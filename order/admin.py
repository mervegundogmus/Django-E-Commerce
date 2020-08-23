from order.models import ShopCart
from django.contrib import admin

# Register your models here.


class ShopCartAdmin(admin.ModelAdmin):
    list_display = ['property','user','quantity']
    list_filter = ['user']


admin.site.register(ShopCart,ShopCartAdmin)