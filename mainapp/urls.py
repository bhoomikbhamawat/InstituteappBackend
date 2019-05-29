from django.conf.urls import  include, url
from django.contrib import admin

from mainapp import views



urlpatterns = [
    url(r'^login$', views.login, ),   
    url(r'^checkreg$', views.checkregister, ),   
    
]
