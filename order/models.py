from django.db import models
from django.contrib.auth.models import User
from property.models import Property
from django.forms import ModelForm, TextInput, Textarea,widgets
from django.contrib.auth.models import User
# Create your models here.

class ShopCart(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    urun = models.ForeignKey(Property,on_delete=models.CASCADE,null=True)
    ay=models.IntegerField()
    def __str__(self):
        return self.urun.title

    @property
    def amount(self):
        return (self.ay*self.urun.price)

    @property
    def price(self):
        return (self.urun.price)


class ShopCartForm(ModelForm):
    class Meta:
        model=ShopCart
        fields=['ay']



class Order(models.Model):
    STATUS=(
        ('New','New'),
        ('Onaylandı','Onaylandı'),
        ('Kiralandı','Kiralandı'),
        ('İptal','İptal'),

    )
    user = models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    total= models.FloatField()
    ip = models.CharField(blank=True,max_length=20)
    status= models.CharField (blank=True,max_length=15, choices=STATUS)
    create_at=models.DateTimeField (auto_now_add=True)
    update_at=models.DateTimeField (auto_now=True)

    def __str__ (self):
        return self.user.username

class OrderProduct(models.Model):
    STATUS = (
        ('New', 'New'),
        ('Onaylandı', 'Onaylandı'),
        ('Kiralandı', 'Kiralandı'),
        ('İptal', 'İptal'),

    )
    order = models.ForeignKey(Order,on_delete=models.CASCADE,null=True)
    user = models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    urun = models.ForeignKey(Property,on_delete=models.CASCADE,null=True)
    ay=models.IntegerField()
    price=models.FloatField()
    amount=models.FloatField()
    status= models.CharField (blank=True,max_length=15, choices=STATUS)
    create_at=models.DateTimeField (auto_now_add=True)
    update_at=models.DateTimeField (auto_now=True)

    def __str__(self):
        return self.urun.title
