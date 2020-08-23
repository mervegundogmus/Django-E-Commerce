from django.utils.safestring import mark_safe
from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
from ckeditor.widgets import CKEditorWidget
from django.forms import ModelForm, TextInput, FileInput
from django.urls import reverse
from django.contrib.auth.models import User
from mptt.models import MPTTModel
from mptt.fields import TreeForeignKey



class Category(MPTTModel):
    STATUS = (
        ('True', 'Evet'),
        ('False', 'Hayir'),
    )
    title = models.CharField(max_length=150)
    keywords = models.CharField(max_length=255)
    description = models.CharField(max_length=30)
    image = models.ImageField(blank=True, upload_to='images/')
    status = models.CharField(max_length=10, choices=STATUS)
    slug = models.SlugField(null=False, unique=True)
    parent = TreeForeignKey('self', blank=True, null=True, related_name='children', on_delete=models.CASCADE)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    class MPTTMeta:
        order_insertion_by = ['title']


    def __str__(self):
        full_path = [self.title]
        k = self.parent
        while k is not None:
            full_path.append(k.title)
            k = k.parent
        return '/'.join(full_path[::-1])

    def image_tag(self):
        return mark_safe('<img src="{}" height="50"/>'.format(self.image.url))

    image_tag.short_description = 'Image'


class Property(models.Model):
    STATUS = (
        ('True', 'Evet'),
        ('False', 'Hayir'),
    )
    category = models.ForeignKey(Category, on_delete=models.CASCADE,null=True)  # relation with Category table
    user = models.ForeignKey(User, on_delete=models.CASCADE,null=True)  # relation with Category table
    title = models.CharField(max_length=150)
    keywords = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    image = models.ImageField(blank=True, upload_to='images/')
    price = models.FloatField(blank=True)
    floor = models.IntegerField(blank=True)
    square_metre = models.FloatField(blank=True)
    room = models.IntegerField(blank=True)
    rate = models.IntegerField(blank=True,null=True)
    address = models.TextField(blank=True,null=True)
    detail = RichTextUploadingField()
    status = models.CharField(max_length=10, choices=STATUS,null=True)
    slug = models.SlugField(null=False, unique=True)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def image_tag(self):
        return mark_safe('<img src="{}" height="50"/>'.format(self.image.url))

    image_tag.short_description = 'Image'

class Images(models.Model):
    property = models.ForeignKey(Property, on_delete=models.CASCADE)
    title = models.CharField(max_length=50, blank=True)
    image = models.ImageField(blank=True, upload_to='images/')

    def __str__(self):
        return self.title

    def image_tag(self):
        return mark_safe('<img src="{}" height="50"/>'.format(self.image.url))

    image_tag.short_description = 'Image'

class Comment(models.Model):
    STATUS = (
        ('New', 'Yeni'),
        ('True', 'Evet'),
        ('False', 'Hayır'),
    )
    property=models.ForeignKey(Property,on_delete=models.CASCADE)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    subject = models.CharField(max_length=50, blank=True)
    comment = models.TextField(max_length=200, blank=True)
    rate = models.IntegerField(blank=True,null=True)
    status=models.CharField(max_length=10,choices=STATUS,default='New')
    ip = models.CharField(blank=True, max_length=20)
    create_at=models.DateTimeField(auto_now_add=True)
    update_at=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.subject

class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ['subject','comment','rate']

class PropertyForm(ModelForm):
    class Meta:
        model = Property
        fields = ['category', 'title', 'keywords', 'price', 'room', 'square_metre', 'floor', 'slug',
                  'description', 'address', 'image', 'detail']
        widgets = {
            'title': TextInput(attrs={'class': 'input', 'placeholder': 'title'}),
            'slug': TextInput(attrs={'class': 'input', 'placeholder': 'slug'}),
            'keywords': TextInput(attrs={'class': 'input', 'placeholder': 'keywords'}),
            'price': TextInput(attrs={'class': 'input', 'placeholder': 'price'}),
            'room': TextInput(attrs={'class': 'input', 'placeholder': 'room'}),
            'rate': TextInput(attrs={'class': 'input', 'placeholder': 'rate'}),
            'floor': TextInput(attrs={'class': 'input', 'placeholder': 'floor'}),
            'square_metre': TextInput(attrs={'class': 'input', 'placeholder': 'floor'}),
            'description': TextInput(attrs={'class': 'input', 'placeholder': 'description'}),
            'address': TextInput(attrs={'class': 'input', 'placeholder': 'address'}),
            'image': FileInput(attrs={'class': 'input', 'placeholder': 'image', }),
            'detail': CKEditorWidget(),

        }

class ImagesForm(ModelForm):
    class Meta:
        model = Images
        fields = ['title','image']
        widgets = {
            'title': TextInput(attrs={'class': 'input', 'placeholder': 'title'}),
            # 'property':ModelChoiceField(queryset=Property.objects.all()),
            'image': FileInput(attrs={'class': 'input', 'placeholder': 'image', }),

        }
class ImageFormContent(ModelForm):
    class Meta:
        model = Images
        fields = ['title','image']