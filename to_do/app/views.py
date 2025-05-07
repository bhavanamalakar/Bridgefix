from django.shortcuts import render,redirect,get_object_or_404
from .models import ToDo
from .forms import ToDoform

def task_list(request):
    tasks=ToDo.objects.all()
    return render(request,'task_list.html',{'tasks':tasks})


def add_task(request):
    if request.method == 'POST':
        task_name=request.POST.get('task')
        new_task= ToDo(task=task_name)
        new_task.save()
        return redirect('task_list')
    return render(request,'add_task.html')

def edit_task(request,pk):
    task=get_object_or_404(ToDo,request.data)
    if request.method=='POST':
        form=ToDoform(request.POST,instance=task)
        if form.is_valid():
            form.save()
            return redirect('task_list')
    else:
        form=ToDoform(instance=task)
    return render(request,'add_task.html',{'task':task})

def delete(request,pk):
    task=get_object_or_404(ToDo,pk=pk)
    task.delete()
    return redirect('task_list')



