
from django.contrib import admin
from .models import Property,Order,OrderProduct,ShopCart
from django import forms
from django.contrib import admin
# Register your models here.

class ShopCartAdmin(admin.ModelAdmin):
    list_display = ['user','urun','price','ay','amount']
    list_filter = ['user']

class OrderProductLine(admin.TabularInline):
    model=OrderProduct
    readonly_fields = ['user','urun','price','ay','amount']
    can_delete=False
    extra=0

class OrderAdmin(admin.ModelAdmin):
    list_display = ['user','status','total','update_at']
    list_filter = ['user']
    readonly_fields=('user','total','update_at','create_at')
    inlines=[OrderProductLine]

admin.site.register(ShopCart,ShopCartAdmin)
admin.site.register(Order,OrderAdmin)