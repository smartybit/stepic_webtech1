from django.shortcuts import render, get_object_or_404
from django.core.urlresolvers import reverse
from django.views.decorators.http import require_POST, require_GET
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import login as login_view
from django.contrib.auth import authenticate, login

from django.http import HttpResponse, HttpResponseRedirect

import qa.dataload as dataload
import qa.models as models
from  qa.pagination import paginate
from forms import AskForm, AnswerForm, SignupForm



def test(request, *args, **kwargs):
    return HttpResponse('OK')

def signup(request, *args, **kwargs):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        username = request.POST['username']
        password = request.POST['password']
        if form.is_valid():
            user = form.save()
            if user.is_active:
                user = authenticate(username=username, password=password)
                login(request, user)
                return HttpResponseRedirect(reverse('mainpage'))
            else:
                return login_view(request, kwargs)
    else:
        form = SignupForm()
    return render(request, 'signup.html', {'form' : form })

def qa_login(request, **kwargs):
    if request.user.is_authenticated():
        return HttpResponseRedirect(reverse('mainpage'))
    else:
        return login_view(request, **kwargs)

def logout(request, **kwargs):
    if request.user.is_authenticated():
        request.session.flush()
    return HttpResponseRedirect(reverse('mainpage'))


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
        if request.user.is_authenticated():
            form = AnswerForm(initial={'question_id': q_id,  'user': request.user})
        else: form = None

    return render(request, 'question.html', {'question': question, 
        'answers': answers, 'form' : form, })

@require_POST
@login_required
def newanswer (request, *args, **kwargs):
    form = AnswerForm(request.POST)
    form.user = request.user
    if form.is_valid():
        question_id = form.save()
        return HttpResponseRedirect(reverse('question', kwargs={'question_id': question_id}))
    else:
        return question(request, **{'form' : form, 'question_id': form.get_question_id()})

@login_required
def newquestion(request, *args, **kwargs):
    if request.method == 'POST':
        form = AskForm(request.POST)
        if form.is_valid():
            form.user = request.user
            question_id = form.save()
            return HttpResponseRedirect(reverse('question', kwargs={'question_id': question_id, }))
    else:
        form = AskForm()
    return render(request, 'newquestion.html', {'form': form})

def createdata(request, *args, **kwargs):
    dataload.createdata()
    return HttpResponse('Data created')
