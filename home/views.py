from django.http import HttpResponse
from django.shortcuts import render
from home.models import Setting
#Create your views here.

def index(request):
    setting = Setting.objects.get(pk=1)
    context = {'setting': setting, 'page':'home'}
    return render(request, 'index.html', context)

def hakkimizda(request):
    setting = Setting.objects.get(pk=1)
    context = {'setting': setting, 'page':'hakkimizda'}
    return render(request, 'hakkimizda.html', context)

def referanslar(request):
    setting = Setting.objects.get(pk=1)
    context = {'setting': setting, 'page':'referanslar'}
    return render(request, 'referanslar.html', context)

def iletişim(request):
    setting = Setting.objects.get(pk=1)
    context = {'setting': setting, 'page':'iletişim'}
    return render(request, 'iletişim.html', context)