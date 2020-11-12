from django.contrib import admin
from django.shortcuts import render
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from series.views import createlanguage, languageedit, languagedelete, createmovie, movieedit, moviedelete, movieview, \
    index,vieworders,orderdetails
from user.views import logOut

urlpatterns = [
    path("", lambda request: render(request, "series/base.html")),
    path('lang/', createlanguage, name='createlanguage'),
    path('langedit<int:pk>/', languageedit, name="languageedit"),
    path('langdel<int:pk>/', languagedelete, name="languagedelete"),
    path('createmovie/', createmovie, name="createmovie"),
    path('editmovie<int:pk>/', movieedit, name="movieedit"),
    path('moviedel<int:pk>/', moviedelete, name="moviedelete"),
    path('movieview<int:pk>', movieview, name="movieview"),
    path('index/', index, name='index'),
    path('vieworder/',vieworders,name='vieworders'),
    path('orderdetails<int:pk>/',orderdetails,name="orderdetails")
]
