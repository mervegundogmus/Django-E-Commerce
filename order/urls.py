from django.urls import path

from . import views

urlpatterns = [
    # ex: /property/
    path('', views.index, name='index')
    # path('addcomment/<int:id>',views.addcomment,name='addcomment'),

    # ex: /polls/5/
    # path('<int:question_id>/', views.detail, name='detail'),
]