from django.contrib import admin
from mptt.admin import DraggableMPTTAdmin

from property.models import Category, Property, Images
# Register your models here.

class PropertyImageInline(admin.TabularInline):
    model = Images
    extra = 5

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['title', 'description','image_tag', 'status']
    readonly_fields = ('image_tag',)
    list_filter = ['status']

class PropertyAdmin(admin.ModelAdmin):
    list_display = ['title', 'category', 'price', 'image_tag' ,'status']
    readonly_fields = ('image_tag',)
    list_filter = ['status', 'category']
    inlines = [PropertyImageInline]
    prepopulated_fields = {'slug': ('title',)}



class ImagesAdmin(admin.ModelAdmin):
    list_display = ['title', 'property', 'image_tag']
    readonly_fields = ('image_tag',)

class CategoryAdmin2(DraggableMPTTAdmin):
    mptt_indent_field = "title"
    list_display = ('tree_actions', 'indented_title',
                    'related_products_count', 'related_products_cumulative_count')
    list_display_links = ('indented_title',)
    prepopulated_fields = {'slug': ('title',)}

    def get_queryset(self, request):
        qs = super().get_queryset(request)

        # Add cumulative product count
        qs = Category.objects.add_related_count(
                qs,
                Property,
                'category',
                'products_cumulative_count',
                cumulative=True)

        # Add non cumulative product count
        qs = Category.objects.add_related_count(
                 qs,
                 Property,
                 'category',
                 'products_count',
                 cumulative=False)
        return qs

    def related_products_count(self, instance):
        return instance.products_count
    related_products_count.short_description = 'Related products (for this specific category)'

    def related_products_cumulative_count(self, instance):
        return instance.products_cumulative_count
    related_products_cumulative_count.short_description = 'Related products (in tree)'


admin.site.register(Category,CategoryAdmin2)
admin.site.register(Property, PropertyAdmin)
admin.site.register(Images, ImagesAdmin)