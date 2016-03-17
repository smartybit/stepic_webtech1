from django.shortcuts import render, get_object_or_404

from django.http import HttpResponse 
import qa.dataload as dataload
import qa.models as models
from  qa.pagination import paginate


def test(request, *args, **kwargs):
    return HttpResponse('OK')


def mainpage(request, *args, **kwargs):
    question_set = models.Question.objects.order_by('-added_at', '-raiting')

    paginator, page = paginate(request, question_set)
    paginator.baseurl = '/?page='
    return render(request, 'mainpage.html', {'questions': page.object_list, 
        'paginator': paginator,
        'page': page})

def popular(request, *args, **kwargs):
    question_set = models.Question.objects.order_by('-raiting', '-added_at')

    paginator, page = paginate(request, question_set)
    paginator.baseurl = '/popular/?page='
    return render(request, 'mainpage.html', {'questions': page.object_list, 
        'paginator': paginator,
        'page': page})
    
def question (request, *args, **kwargs):

    try: q_id = int(kwargs['question_id'])
    except: q_id = -1
    question = get_object_or_404(models.Question, id = q_id)
    try: 
        answers = models.Answer.objects.filter(question_id = q_id).order_by('-added_at')
    except:
        answers = None
    return render(request, 'question.html', {'question': question, 
        'answers': answers, })
    


def createdata(request, *args, **kwargs):
    dataload.createdata()
    return HttpResponse('Data created')
