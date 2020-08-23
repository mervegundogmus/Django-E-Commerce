from django.shortcuts import render
from django.http import HttpResponse
from property.models import  Category
# Create your views here.
def index(request):
    category = Category.objects.all()
    context = {'category': category}
    return render(request, 'user_profile.html', context)


