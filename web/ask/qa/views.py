from django.shortcuts import render

from django.http import HttpResponse 

def test(request, *args, **kwargs):
    return HttpResponse('OK')


def mainpage(request, *args, **kwargs):
    try:
        pagenum = request.GET.get('page')
    except:
        pagenum = 0
    return HttpResponse('OK: ' + pagenum)
