from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('home/',views.home,name="blog"),
    path('about/',views.about,name="blog"),
    path('',views.base,name="empty")
    
]