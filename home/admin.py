from django.contrib import admin

from home.models import Setting, ContactFormMessage
from home.models import UserProfile

class ContactFormMessageAdmin(admin.ModelAdmin):
    list_display = ['name', 'email','subject','message','note','status']
    list_filter = ['status']

class UserProfileAdmin(admin.ModelAdmin):
    list_display = ['user_name','phone','address','city','country','image_tag']


admin.site.register(ContactFormMessage, ContactFormMessageAdmin)
admin.site.register(Setting)
admin.site.register(UserProfile, UserProfileAdmin)