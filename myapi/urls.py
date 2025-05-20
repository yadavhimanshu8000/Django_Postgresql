"""
URL configuration for myproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from django.contrib import admin
from django.urls import path,include
from myapi.views import *
from rest_framework.urlpatterns import format_suffix_patterns


urlpatterns = [
    
    path('createuser/', Userview.as_view()),
    path('createuser/<int:pk>/', Usercurd.as_view()),
    
    path('category/', Categoryview.as_view()),
    
    path('shipment/', Shipmentview.as_view()),
    
    path('product/', Productview.as_view()),
    path('product/<int:pk>/', Productcurd.as_view()),
    
    path('payment/', Paymentview.as_view()),
    
    path('order/', Orderview.as_view()),
    
    path('orderitem/', Order_item_view.as_view()),
    path('orderitem/<int:pk>/', Order_item_curd.as_view()),
    
    path('cart/', Cartview.as_view()),
    path('cart/<int:pk>/', Cartcurd.as_view()),
    
    path('wishlist/', Wishlistview.as_view()),
    path('wishlist/<int:pk>/', Wishlistcurd.as_view()),
    
   
]
urlpatterns = format_suffix_patterns(urlpatterns)
