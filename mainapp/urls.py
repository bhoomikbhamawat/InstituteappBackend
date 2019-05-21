from django.conf.urls import  include, url
from django.contrib import admin

from mainapp import views



urlpatterns = [
	url(r'^users/', views.UserList.as_view()),
	url(r'^users/(?P<pk>[0-9]+)/$', views.UserDetail.as_view())
]
