from django.shortcuts import render

from django.http import HttpResponse 
import qa.dataload as dataload
import qa.models as models
from  qa.pagination import paginate


def test(request, *args, **kwargs):
    return HttpResponse('OK')


def mainpage(request, *args, **kwargs):
    question_set = models.Question.objects.order_by('raiting')
    paginator, page = paginate(request, question_set)
    paginator.baseurl = '/?page='
    return render(request, 'mainpage.html', {'questions': page.object_list, 
        'paginator': paginator,
        'page': page})
    


def createdata(request, *args, **kwargs):
    dataload.createdata()
    return HttpResponse('Data created')
