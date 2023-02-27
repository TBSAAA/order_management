"""order_management URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# from django.contrib import admin
from django.urls import path
from web.views import account, user,order,level,product
from web.views import jack

urlpatterns = [
    path('', account.jack_home, name='jack_home'),
    path('study/experience/', jack.study_experience, name='jack_experience'),


    path('login/', account.login, name='login'),
    path('get_code/', account.get_code, name='get_code'),
    path('register/', account.register, name='register'),
    path('logout/', account.logout, name='logout'),
    path('index/', account.index, name='index'),
    path('home/', account.home, name='home'),

    path('user/list/', user.user_list, name='user_list'),
    path('user/add/', user.user_add, name='user_add'),
    path('user/edit/<int:uid>/', user.user_edit, name='user_edit'),
    path('user/del/<int:uid>/', user.user_delete, name='user_delete'),

    path('order/list/', order.order_list, name='order_list'),
    path('order/add/', order.order_add, name='order_add'),
    path('order/edit/<int:uid>/', order.order_edit, name='order_edit'),
    path('order/del/<int:uid>/', order.order_delete, name='order_delete'),

    path('level/list/', level.level_list, name='level_list'),
    path('level/add/', level.level_add, name='level_add'),
    path('level/edit/<int:uid>/', level.level_edit, name='level_edit'),
    path('level/del/<int:uid>/', level.level_delete, name='level_delete'),

    path("product/list/", product.product_list, name="product_list"),
    path("product/add/", product.product_add, name="product_add"),
    path("product/edit/<int:uid>/", product.product_edit, name="product_edit"),
    path("product/del/<int:uid>/", product.product_delete, name="product_delete"),





]
