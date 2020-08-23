from django.urls import path

from . import views

urlpatterns = [
    # ex: /property/
    path('', views.index, name='index'),
    # path('addcomment/<int:id>',views.addcomment,name='addcomment'),

    path('update/', views.user_update, name='user_update'),
    path('password/', views.change_password, name='change_password'),

    path('comments/', views.comments, name='comments'),
    path('deletecomment/<int:id>', views.deletecomment,name='deletecomment'),

    path('contents/', views.contents,name='contents'),
    path('deletecontent/<int:id>', views.deletecontent,name='deletecontent'),
    path('editcontent/<int:id>', views.editcontent,name='editcontent'),
    path('addgaleri/<int:id>', views.addgaleri,name='addgaleri'),
    path('addcontent/', views.addcontent,name='addcontent'),

    path('shopcart/', views.shopcart, name='shopcart'),

    path('orders/', views.orders, name='orders'),
    path('orderdetail/<int:id>', views.orderdetail, name='orderdetail'),

    # ex: /polls/5/
    # path('<int:question_id>/', views.detail, name='detail'),
]