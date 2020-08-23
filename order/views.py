from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages
from order.models import ShopCartForm
from order.models import ShopCart, Order, OrderProduct
from django.contrib.auth.decorators import login_required
from home.models import Setting
from property.models import Category, Property


# Create your views here.
def index(request):
    return HttpResponse("Order Page")


@login_required(login_url='/login')
def addurun(request, id):
    url = request.META.get("HTTP_REFERER")
    if request.method == 'POST':
        form = ShopCartForm(request.POST)
        if form.is_valid():
            current_user = request.user
            if (ShopCart.objects.filter(urun_id=id)):
                data = ShopCart.objects.get(urun_id=id)
                data.ay += form.cleaned_data['ay']
                data.save()
            else:
                data = ShopCart()
                data.user_id = current_user.id
                data.urun_id = id
                data.ay = form.cleaned_data['ay']
                data.save()
            request.session['cart_item'] = ShopCart.objects.filter(user_id=current_user.id).count()
        messages.success(request, "Ev başarıyla eklendi.")
        return HttpResponseRedirect(url)

    else:
        messages.warning(request, "Ev gönderilemedi. Lütfen tekrar deneyiniz belirtiniz.")
        return HttpResponseRedirect(url)





@login_required(login_url='/login')
def deletefromcart(request, id):
    current_user = request.user
    ShopCart.objects.filter(id=id).delete()
    messages.success(request, 'Ev sepetden silinmistir')
    request.session['cart_item'] = ShopCart.objects.filter(user_id=current_user.id).count()
    return HttpResponseRedirect('/user/shopcart')


@login_required(login_url='/login')
def siparis(request,id):
    setting = Setting.objects.get(pk=1)
    category = Category.objects.all()

    current_user = request.user #su anki userin bilgilerini aliyor
    schopcart=ShopCart.objects.get(pk=id)
    total=schopcart.ay*schopcart.urun.price
    if id: #shopcartdan id gelmisse
        data = Order()# order modeline baglaniyor
        data.user_id = current_user.id #bilgileri Order veritabanina aktariyor
        data.status = 'New'
        data.total=total
        data.ip = request.META.get('REMOTE_ADDR')
        data.save()#aktarilan verileri kayd ediyor

        schopcart = ShopCart.objects.get(pk=id) #Shopcartdan gelen  idli veriyi OrderProducta ekliyor
        #orderproducta ekleme
        detail = OrderProduct()#orderproductta baglaniiyor
        detail.order_id = data.id
        detail.urun_id = schopcart.urun_id
        detail.user_id = current_user.id
        detail.ay = schopcart.ay
        detail.price = schopcart.urun.price
        detail.amount = schopcart.amount
        detail.status = 'New'
        detail.save()
        ShopCart.objects.get(pk=id).delete()#shopcartdan alinan veriyi siliyor
        prodata=Property.objects.get(pk=schopcart.urun_id)#shopcartdan sifaris verilen urunu aliyor
        prodata.status="False"#statusunu flase yapiyor
        prodata.save()
        messages.success(request, 'Sifarisiniz Basariyla Alinmistir')#basarili islem mesaji
        context = {
            'setting': setting,
            'category' : category,
            'shopcart': schopcart,
            'total': total,
        }
        return HttpResponseRedirect('/user/orders')#user orderse gonderiyor
    else:
        messages.warning(request, "Siparis Alinamadi")#basarisiz islem
        return HttpResponseRedirect('/user/shopcart')#shopcartda kaliyor
