from django.contrib import admin

# Register your models here.
from property.models import Category, Property, Images


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['title', 'description', 'status']
    list_filter = ['status']

class PropertyAdmin(admin.ModelAdmin):
    list_display = ['title', 'category', 'price', 'amount', 'status']
    list_filter = ['status', 'category']

admin.site.register(Category,CategoryAdmin)
admin.site.register(Property, PropertyAdmin)
admin.site.register(Images)
