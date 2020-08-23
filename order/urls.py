from django.urls import path

from . import views

urlpatterns = [
    # ex: /property/
    path('', views.index, name='index'),
    path('addurun/<int:id>', views.addurun, name='addurun'),
    path('deletefromcart/<int:id>', views.deletefromcart, name='deletefromcart'),
    path('siparis/<int:id>', views.siparis, name='siparis')

]