from django.http import HttpResponse
from django.shortcuts import render
from home.models import Setting
#Create your views here.

def index(request):
    setting = Setting.objects.get(pk=1)
    context = {'setting': setting}
    return render(request, 'index.html', context)