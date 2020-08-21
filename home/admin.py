from django.contrib import admin
from home.models import UserProfile
# Register your models here.
from home.models import Setting

class UserProfileAdmin(admin.ModelAdmin):
    list_display = ['user_name','phone','address','city','country','image_tag']

admin.site.register(Setting)
admin.site.register(UserProfile, UserProfileAdmin)

