from django.http import HttpResponse

from .models import Question,Choice

def index(request):
    latest_question_list= Question.objects.order_by('-pub_date')[:5]
    output=','.join([q.question_text for q in latest_question_list])
    
    return HttpResponse(output)
    # return HttpResponse("hello,this is first try view")
    



def detail(request,question_id):
    return HttpResponse("You're looking at questiobs %s." % question_id)

def results(request,question_id):
    response="You're looking at the results of question%s."
    return HttpResponse(response % question_id)

def vote(request,question_id):
    return HttpResponse("you're voting on question %s." % question_id)
