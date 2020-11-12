from django.contrib import admin
from django.shortcuts import render
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from series.views import createlanguage, languageedit, languagedelete, createmovie, movieedit, moviedelete, movieview, \
    index
from user.views import usermovieview, userindex, userorder, register, loginpage, logOut,uservieworders

urlpatterns = [
    path("1", lambda request:render(request, "user/userbase.html")),
    # path('lang/', createlanguage, name='createlanguage'),
    # path('langedit<int:pk>/', languageedit, name="languageedit"),
    # path('langdel<int:pk>/', languagedelete, name="languagedelete"),
    # path('createmovie/', createmovie, name="createmovie"),
    # path('editmovie<int:pk>/', movieedit, name="movieedit"),
    # path('moviedel<int:pk>/', moviedelete, name="moviedelete"),
    # path('movieview<int:pk>', movieview, name="movieview"),
    path('userindex/', userindex, name='userindex'),
    path('usermovieview<int:pk>/', usermovieview, name="usermovieview"),
    path('order<int:pk>/',userorder,name="userorder"),
    path('uservieworder', uservieworders, name='uservieworders'),
    path('register',register,name="register"),
    path('',loginpage,name="loginpage"),
    path('logout/',logOut,name="logout"),


]
