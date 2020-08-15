from django.contrib import admin
from mptt.admin import MPTTModelAdmin, DraggableMPTTAdmin

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
    list_display = ['title', 'category', 'price', 'amount', 'image_tag' ,'status']
    readonly_fields = ('image_tag',)
    list_filter = ['status', 'category']
    inlines = [PropertyImageInline]


class ImagesAdmin(admin.ModelAdmin):
    list_display = ['title', 'property', 'image_tag']
    readonly_fields = ('image_tag',)

class CategoryAdmin2(DraggableMPTTAdmin):
    mptt_indent_field = "title"
    list_display = ('tree_actions', 'indented_title',
                     'related_propertys_count', 'related_propertys_cumulative_count')
    list_display_links = ('indented_title',)

    def get_queryset(self, request):
        qs = super().get_queryset(request)

        # Add cumulative product count
        qs = Category.objects.add_related_count(
            qs,
            Property,
            'category',
            'propertys_cumulative_count',
            cumulative=True)

        # Add non cumulative product count
        qs = Category.objects.add_related_count(qs,
                                                Property,
                                                'category',
                                                'propertys_count',
                                                cumulative=False)
        return qs

    def related_propertys_count(self, instance):
        return instance.propertys_count
    related_propertys_count.short_description = 'Related propertys (for this specific category)'

    def related_propertys_cumulative_count(self, instance):
        return instance.propertys_cumulative_count
    related_propertys_cumulative_count.short_description = 'Related propertys (in tree)'


admin.site.register(Category,CategoryAdmin2)
admin.site.register(Property, PropertyAdmin)
admin.site.register(Images, ImagesAdmin)
