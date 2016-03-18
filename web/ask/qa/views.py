from django.shortcuts import render, get_object_or_404
from django.core.urlresolvers import reverse
from django.views.decorators.http import require_POST, require_GET

from django.http import HttpResponse, HttpResponseRedirect 
import qa.dataload as dataload
import qa.models as models
from  qa.pagination import paginate
from forms import AskForm, AnswerForm



def test(request, *args, **kwargs):
    return HttpResponse('OK')


def mainpage(request, *args, **kwargs):
    question_set = models.Question.objects.order_by('-added_at', '-rating')

    paginator, page = paginate(request, question_set)
    paginator.baseurl = '/?page='
    return render(request, 'mainpage.html', {'questions': page.object_list, 
        'paginator': paginator,
        'page': page})

def popular(request, *args, **kwargs):
    question_set = models.Question.objects.order_by('-rating', '-added_at')

    paginator, page = paginate(request, question_set)
    paginator.baseurl = '/popular/?page='
    return render(request, 'mainpage.html', {'questions': page.object_list, 
        'paginator': paginator,
        'page': page})
    
def question (request, *args, **kwargs):

    try: q_id = int(kwargs['question_id'])
    except: q_id = -1
    q_id = int(kwargs['question_id'])
    question = get_object_or_404(models.Question, id = q_id)
    try: 
        answers = models.Answer.objects.filter(question_id = q_id).order_by('-added_at')
    except:
        answers = None
    if 'form' in kwargs:
        form = kwargs['form']
    else:
        form = AnswerForm(initial={'question_id': q_id, 'author_id' : 2})
    return render(request, 'question.html', {'question': question, 
        'answers': answers, 'form' : form, })

@require_POST
def newanswer (request, *args, **kwargs):
    form = AnswerForm(request.POST)
    if form.is_valid():
        question_id = form.save()
        return HttpResponseRedirect(reverse('question', kwargs={'question_id': question_id}))
    else:
        deb = form.get_question_id()
        return question(request, **{'form' : form, 'question_id': form.get_question_id()})

def newquestion(request, *args, **kwargs):
    if request.method == 'POST':
        form = AskForm(request.POST)
        if form.is_valid():
            question_id = form.save()
            return HttpResponseRedirect(reverse('question', kwargs={'question_id': question_id}))
    else:
        form = AskForm()
    return render(request, 'newquestion.html', {'form': form})

def createdata(request, *args, **kwargs):
    dataload.createdata()
    return HttpResponse('Data created')
