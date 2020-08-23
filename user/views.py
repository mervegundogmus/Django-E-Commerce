from django.shortcuts import redirect, render
from django.http import HttpResponse, HttpResponseRedirect
from property.models import  Category,Comment,Property,Images, ImageFormContent,PropertyForm
from home.models import  Setting,UserProfile
from order.models import  ShopCart,Order,OrderProduct

from django.contrib.auth.forms import PasswordChangeForm

from django.contrib import messages
from user.form import UserUpdateForm,ProfileUpdateForm

from django.contrib.auth.decorators import login_required
from django.contrib.auth import update_session_auth_hash
# Create your views here.
@login_required(login_url='/login')
def index(request):
    current_user = request.user
    category = Category.objects.all()
    profile = UserProfile.objects.get(user_id=current_user.id)
    setting = Setting.objects.get(pk=1)
    context = {'category': category,
               'setting': setting,
               'profile': profile,
               }
    return render(request, 'user_profile.html', context)


@login_required(login_url='/login') # Check togin
def comments (request):
    category = Category.objects.all()
    setting = Setting.objects.get(pk=1)
    current_user = request.user
    comments = Comment.objects.filter(user_id=current_user.id)
    context = {
        'category': category,
        'setting': setting,
        'comments': comments,
      }
    return render(request, 'user_comment.html', context)


@login_required(login_url='/login')
def deletecontent(request, id):
    Property.objects.filter(id=id).delete()
    messages.warning(request, "Ilan  silinmiştir.")
    return HttpResponseRedirect("/user/contents")

@login_required(login_url='/login')
def deletecomment(request,id):
    Comment.objects.filter(id=id).delete()
    messages.warning(request,"Yorumunuz  silinmiştir.")
    return HttpResponseRedirect("/user/comments")

@login_required(login_url='/login')
def contents(request):
    category = Category.objects.all()
    setting = Setting.objects.get(pk=1)
    current_user = request.user
    contents = Property.objects.filter(user_id=current_user.id).order_by('-update_at')
    context = {
        'category': category,
        'setting': setting,
        'contents': contents,
      }
    return render(request, 'user_propertys.html', context)


@login_required(login_url='/login')
def addcontent(request):
    if request.method == 'POST':
        form = PropertyForm(request.POST, request.FILES)
        if form.is_valid():
            current_user = request.user
            data = Property()
            data.category= form.cleaned_data['category']
            data.user_id = current_user.id
            data.title = form.cleaned_data['title']
            data.keywords = form.cleaned_data['keywords']
            data.description = form.cleaned_data['description']
            data.price = form.cleaned_data['price']
            data.square_metre = form.cleaned_data['square_metre']
            data.room = form.cleaned_data['room']
            data.floor = form.cleaned_data['floor']
            data.status = 'New'
            data.address = form.cleaned_data['address']
            data.slug = form.cleaned_data['slug']
            data.image = form.cleaned_data['image']
            data.detail = form.cleaned_data['detail']
            data.save()
            messages.success(request, "İçerik başarıyla eklendi")
            return HttpResponseRedirect("/user/contents")
        else:
            messages.warning(request, "İçerik eklenmedi" + str(form.errors))
            return HttpResponseRedirect("/user/contents")


    else:
        form = PropertyForm()
        category = Category.objects.all()
        setting = Setting.objects.get(pk=1)
        context = {
            'category': category,
            'setting': setting,
            'form': form,
        }
        return render(request, 'user_addproperty.html', context)

@login_required(login_url='/login')
def editcontent(request, id):
    content = Property.objects.get(id=id)
    if request.method == 'POST':
        form = PropertyForm(request.POST, request.FILES, instance=content)
        if form.is_valid():
            form.save()
            messages.success(request, "İçerik başarıyla düzenlendi")
            return HttpResponseRedirect("/user/contents")
        else:
            messages.warning(request, "İçerik düzenlenemedi" + str(form.errors))
            return HttpResponseRedirect("/user/editcontent" + str(id))


    else:
        form = PropertyForm(instance=content)
        category = Category.objects.all()
        setting = Setting.objects.get(pk=1)
        context = {
            'category': category,
            'setting': setting,
            'form': form,
        }
        return render(request, 'user_editproperty.html', context)

def addgaleri(request,id):
    if request.method=='POST':
        lasturl=request.META.get('HTTP_REFERER')
        form =ImageFormContent(request.POST,request.FILES)
        if form.is_valid():
            data=Images()
            data.title=form.cleaned_data['title']
            data.property_id=id
            data.image=form.cleaned_data['image']
            data.save()
            messages.success(request, 'Resim yuklendi')
            return HttpResponseRedirect(lasturl)
        else:
            messages.warning(request, 'Yukleme hatasi.<br>'+str(form.errors))
            return HttpResponseRedirect(lasturl)

    else:
        content=Property.objects.get(id=id)
        image=Images.objects.filter(urun_id=id)
        context={
            'content':content,
            'images':image,
            'form':ImageFormContent()
        }
        return render(request,'user_galeri.html',context)

@login_required(login_url='/login')
def user_update(request):
    if request.method == 'POST':
        user_form=UserUpdateForm(request.POST, instance=request.user)
        profile_form=ProfileUpdateForm(request.POST,request.FILES,instance=request.user.userprofile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request,"Profiliniz Guncellendi")
            return redirect('/user')

    else:
        user_form=UserUpdateForm(instance=request.user)
        profile_form=ProfileUpdateForm(instance=request.user.userprofile)
        category = Category.objects.all()
        setting = Setting.objects.get(pk=1)
        context={
            'category': category,
            'user_form': user_form,
            'setting': setting,
            'profile_form':profile_form,
        }
        return render(request,'user_update.html',context)


@login_required(login_url='/login')
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            messages.success(request, 'Şifreniz başarıyla değiştirildi')
            return redirect('/user')
        else:
            messages.warning(request, 'Lütfen hatalara dikkat ediniz.<br>' + str(form.errors))

    category = Category.objects.all()
    setting = Setting.objects.get(pk=1)
    form = PasswordChangeForm(request.user)
    context = {
        'category': category,
        'setting': setting,
        'form': form,
    }
    return render(request, 'change_password.html', context)

@login_required(login_url='/login')
def shopcart(request):
    curent_user = request.user
    schopcart = ShopCart.objects.filter(user_id=curent_user.id)
    total = 0;
    for rs in schopcart:
        total += rs.urun.price * rs.ay
    setting = Setting.objects.get(pk=1)
    category = Category.objects.all()

    context = {
        'setting': setting,
        'category' : category,
        'shopcart': schopcart,
        'total': total,
    }
    request.session['cart_item'] = ShopCart.objects.filter(user_id=curent_user.id).count()
    return render(request, 'shopcart.html', context)

@login_required(login_url='/login')
def orders(request):
    setting = Setting.objects.get(pk=1)
    category = Category.objects.all()
    current_user = request.user
    orders = OrderProduct.objects.filter(user_id=current_user.id).order_by('-update_at')
    context = {
        'setting': setting,
        'category' : category,
        'orders': orders,
      }
    return render(request, 'user_order.html', context)
@login_required(login_url='/login')
def orderdetail(request,id):
    current_user = request.user
    orders=OrderProduct.objects.filter(order_id=id)
    context = {
        'orders': orders
      }
    return render(request,'orderdetail.html',context)
