from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from home.models import Setting
from property.models import Property, Category, Images
from django.db.models import Count
from django.contrib import messages
#Create your views here.

def index(request):
    setting = Setting.objects.get(pk=1)
    sliderdata = Property.objects.all()[:6]
    category = Category.objects.all()
    property = Property.objects.all()[:9]
    context = {'setting': setting,
               'page':'home',
               'sliderdata': sliderdata,
               'category' : category,
               'property': property}
    return render(request, 'index.html', context)

def propertys(request):
    setting = Setting.objects.get(pk=1)
    category = Category.objects.all()
    property = Property.objects.all()
    context = {'setting': setting,
               'category' : category,
               'property': property}
    return render(request, 'propertys.html', context)

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

def ilanlar(request):
    setting = Setting.objects.get(pk=1)
    category = Category.objects.all()
    property = Property.objects.all()[:9]
    context = {'setting': setting,
               'category': category,
               'page':'ilanlar',
               'property': property}
    return render(request, 'ilanlar.html', context)



def category_propertys(request, id, slug):
    setting = Setting.objects.get(pk=1)
    category = Category.objects.all()
    categorydata = Category.objects.get(pk=id)
    propertys = Property.objects.filter(category_id=id),
    context = {'propertys': propertys,
               'setting': setting,
                'categorydata': categorydata,
                'category' : category,
                'slug': slug}
    return render(request, 'propertys.html', context)

def property_detail(request,id,slug):
    mesaj="Ürün" ,id,"/",slug
    return HttpResponse(mesaj)