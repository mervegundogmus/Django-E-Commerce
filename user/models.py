from django.db import models
from django.contrib.auth.models import User
from django.utils.safestring import mark_safe

# Create your models here.

class UserProfile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    phone = models.CharField(blank=True, max_length=20)
    facebook = models.CharField(blank=True, max_length=20)
    email = models.CharField(blank=True, max_length=20)
    skype = models.CharField(blank=True, max_length=20)
    contact_detail = models.CharField(blank=True, max_length=150)
    biography = models.CharField(blank=True, max_length=150)
    image = models.ImageField(blank=True,upload_to='images/users/')

    def __str__(self):
        return self.user.username

    def user_name(self):
        return '['+self.user.username + '] ' + self.user.first_name +' '+ self.user.last_name

    def image_tag(self):
        if self.image:
            return mark_safe('<img src="{}" height="50"/>'.format(self.image.url))
        else:
            return 'No image Found'

    image_tag.short_desciription = 'image'

