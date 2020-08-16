from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from home.models import Setting
from property.models import Property, Category
from django.db.models import Count
from django.contrib import messages
#Create your views here.

def index(request):
    setting = Setting.objects.get(pk=1)
    sliderdata = Property.objects.all()[:3]
    category = Category.objects.all()
    context = {'setting': setting,
               'page':'home',
               'sliderdata': sliderdata,
               'category' : category}
    return render(request, 'index.html', context)

def hakkimizda(request):
    setting = Setting.objects.get(pk=1)
    category = Category.objects.all()
    context = {'setting': setting, 'category': category, 'page':'hakkimizda'}
    return render(request, 'hakkimizda.html', context)

def referanslar(request):
    setting = Setting.objects.get(pk=1)
    category = Category.objects.all()
    context = {'setting': setting, 'category': category, 'page':'referanslar'}
    return render(request, 'referanslar.html', context)

def iletisim(request):
    setting = Setting.objects.get(pk=1)
    category = Category.objects.all()
    context = {'setting': setting, 'category': category, 'page':'iletisim'}
    return render(request, 'iletisim.html', context)

def category_propertys(request, id, slug):
    category = Category.objects.all()
    categorydata = Category.objects.get(pk=id)
    propertys = Property.objects.filter(category_id=id),
    context = {'propertys': propertys,
               'categorydata': categorydata,
               'category' : category,
               'slug': slug
               }
    return render(request, 'propertys.html', context)