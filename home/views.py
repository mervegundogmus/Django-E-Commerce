from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from home.models import Setting, ContactFormu, ContactFormMessage
from property.models import Property, Category, Images, Comment
from django.contrib.auth import logout, authenticate, login, forms
from home.form import SearchForm, SignUpForm

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
    if request.method == 'POST': # form post edildiyse
        form = ContactFormu(request.POST)
        if form.is_valid():
            data = ContactFormMessage() # model ile bağlantı kur
            data.name = form.cleaned_data['name'] #formdan bilgiyi al
            data.email = form.cleaned_data['email']
            data.subject = form.cleaned_data['subject']
            data.message = form.cleaned_data[ 'message' ]
            data.ip = request.META.get('REMOTE_ADDR')
            data.save() # verirabanına kaydet
            messages.success(request, "Mesajanız başarı ile gönderilmiştir. Teşekkür Ederiz ")
            return HttpResponseRedirect('/iletisim')



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
                'form': form,
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

def signup_view(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return HttpResponseRedirect('/')

    form = SignUpForm()
    category = Category.objects.all()
    context = {'category': category,
               'form': form,
                   }
    return render(request,'signup.html',context)