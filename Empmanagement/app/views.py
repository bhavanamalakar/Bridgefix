from django.shortcuts import render,redirect,get_object_or_404
from .models import Employee
from forms import Empform


def Emp_list(request):
    employee=Employee.objects.all()
    return render(request,'Emplist.html',{'e':employee})

def create_emp(request):
    if request.method=='POST':
        e=Employee.objects.get(request.data)
        form = Empform()
        if form.is_valid():
            form.save()
            return redirect('Emplist')
        
    else:
        form=Empform()
    return render(request,'Add_emp.html',{'e':e})

def update_emp(request,pk):
    emp=get_object_or_404(Employee,pk=pk)
    if request.method=='POST':
        form=Empform(request.data,instance=emp)
        if form.is_valid():
            form.save()
            return redirect('Emplist')
    else:
        return render(request,'Add_emp.html',{'form':form})
    
def delete_emp(request,pk):
    emp=get_object_or_404(Employee,pk=pk)
    emp.delete()
    return redirect('Emplist')






