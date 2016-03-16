from django.shortcuts import render

from django.http import HttpResponse 
import qa.dataload as dataload


def test(request, *args, **kwargs):
    return HttpResponse('OK')


def mainpage(request, *args, **kwargs):
    try:
        pagenum = request.GET.get('page')
    except:
        pagenum = 0
    return HttpResponse('OK: ' + pagenum)


def createdata(request, *args, **kwargs):
    dataload.createdata()
    return HttpResponse('Data created')
