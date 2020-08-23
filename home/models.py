from django.contrib.auth.models import User
from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
from django.forms import ModelForm, TextInput, Textarea
from django.utils.safestring import mark_safe


# Create your models here.

class Setting(models.Model):
    STATUS = (
        ('True', 'Evet'),
        ('False', 'Hayir'),
    )
    title = models.CharField(max_length=150)
    keywords = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    company = models.CharField(blank=True, max_length=150)
    address = models.CharField(blank=True, max_length=150)
    phone = models.CharField(blank=True, max_length=15)
    fax = models.CharField(blank=True, max_length=15)
    email = models.CharField(blank=True, max_length=50)
    smtpserver = models.CharField(blank=True, max_length=20)
    smtpemail = models.CharField(blank=True, max_length=20)
    smtppassword = models.CharField(blank=True, max_length=10)
    smtpport = models.CharField(blank=True, max_length=5)
    icon = models.ImageField(blank=True, upload_to='images/')
    facebook = models.CharField(blank=True, max_length=50)
    twitter = models.CharField(blank=True, max_length=50)
    aboutus = RichTextUploadingField(blank=True)
    contact = RichTextUploadingField(blank=True)
    references = RichTextUploadingField(blank=True)
    status = models.CharField(max_length=10, choices=STATUS)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=20)
    address = models.CharField(max_length=150)
    city = models.CharField(max_length=20)
    country = models.CharField(max_length=20)
    image = models.ImageField(blank=True, upload_to='images/users/')

    def __str__(self):
        return self.user.username

    def user_name(self):
        return '['+self.user.username + '] ' + self.user.first_name +' '+ self.user.last_name

    def image_tag(self):
        return mark_safe('<img src="{}" height="50"/>'.format(self.image.url))

    image_tag.short_description='Image'

class UserProfileForm(ModelForm):
    class Meta:
        model=UserProfile
        fields = ['phone','address','city','country','image']


class ContactFormMessage(models.Model):
    STATUS = (
        ('New', 'New'),
        ('Read', 'Read'),
        ('Closed', 'Closed'),
    )
    name = models.CharField(blank=True, max_length=20)
    email = models.CharField(blank=True, max_length=50)
    subject = models.CharField(blank=True, max_length=50)
    message = models.CharField(blank=True, max_length=255)
    status = models.CharField(max_length=10, choices=STATUS, default='New')
    ip = models.CharField(blank=True, max_length=20)
    note = models.CharField(blank=True, max_length=100)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class ContactFormu(ModelForm):
    class Meta:
        model = ContactFormMessage
        fields = ['name', 'email', 'subject', 'message']
        widgets = {
            'name': TextInput(attrs={'type': 'text', 'name': 'name', 'placeholder': 'Isim Soyisim'}),
            'email': TextInput(attrs={'type': 'email', 'name': 'email', 'placeholder': 'Email'}),
            'subject': TextInput(attrs={'type': 'text', 'name': 'subject', 'placeholder': 'Subject'}),
            'message': Textarea(attrs={'name': 'message', 'placeholder': 'Your Message'}),
        }
