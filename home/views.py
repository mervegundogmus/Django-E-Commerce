from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from home.models import Setting
from property.models import Property, Category, Images, Comment
from django.contrib.auth import logout, authenticate, login


from django.db.models import Count
from django.contrib import messages
#Create your views here.

def index(request):
    setting = Setting.objects.get(pk=1)
    sliderdata = Property.objects.all()[:6]
    category = Category.objects.all()
    daypropertys = Property.objects.all()[:3]
    lastpropertys = Property.objects.all().order_by('-id')[:3]
    context = {'setting': setting,
               'page':'home',
               'sliderdata': sliderdata,
               'category' : category,
               'daypropertys' : daypropertys,
               'lastpropertys': lastpropertys
               }
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


def ilanlar(request, id):
    setting = Setting.objects.get(pk=1)
    category = Category.objects.all()
    if id is not 0:
        property = Property.objects.filter(category_id=id)
    else:
        property = Property.objects.all()[:9]
    context = {'setting': setting,
               'category': category,
               'page':'ilanlar',
               'property': property}
    return render(request, 'ilanlar.html', context)


# Problemli metod
def category_propertys(request, id, slug):
    setting = Setting.objects.get(pk=1)
    category = Category.objects.all()
    categorydata = Category.objects.get(pk=id)
    property = Property.objects.all()[:9],
    print(propertys)
    context = {'property': property,
               'setting': setting,
                'categorydata': categorydata,
                'category' : category,
                'slug': slug}
    return render(request, 'ilanlar.html', context)

def property_detail(request,id,slug):
    category = Category.objects.all()
    property = Property.objects.get(pk=id)
    images = Images.objects.filter(property_id=id)
    context = {'property': property,
               'category' : category,
               'images' : images,
               }
    return render(request, 'property_detail.html', context)

def property_search(request):
    if request.method == 'POST': # form post edildiyse
        form = SearchForm(request.POST)
        if form.is_valid():
            category = Category.objects.all()
            query = form.cleaned_data['query'] #formdan bilgiyi al
            propertys = Property.objects.filter(title__icontains=query)
            context = {
                'propertys': propertys,
                'category': category,
            }
            return render(request, 'propertys_search.html', context)
    return HttpResponseRedirect('/')

def logout_view(request):
    logout(request)
    return HttpResponseRedirect('/')

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            # Redirect to a success page.
            return HttpResponseRedirect('/')
        else:
            messages.warning(request, "Login Hatasi ! Kullanici Adi veya sifre yanlis")
            return HttpResponseRedirect ('/login')

    setting = Setting.objects.get(pk=1)
    category = Category.objects.all()
    context = { 'setting':setting,'category': category,}
    return render(request,'login.html',context)

