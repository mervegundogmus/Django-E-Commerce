from django.contrib import admin


# Register your models here.
from property.models import Category, Property, Images

class PropertyImageInline(admin.TabularInline):
    model = Images
    extra = 5

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['title', 'description','image_tag', 'status']
    readonly_fields = ('image_tag',)
    list_filter = ['status']

class PropertyAdmin(admin.ModelAdmin):
    list_display = ['title', 'category', 'price', 'amount', 'image_tag' ,'status']
    readonly_fields = ('image_tag',)
    list_filter = ['status', 'category']
    inlines = [PropertyImageInline]


class ImagesAdmin(admin.ModelAdmin):
    list_display = ['title', 'property', 'image_tag']
    readonly_fields = ('image_tag',)

admin.site.register(Category,CategoryAdmin)
admin.site.register(Property, PropertyAdmin)
admin.site.register(Images, ImagesAdmin)
