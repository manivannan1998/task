from django.contrib import admin
from django.urls import path
from . import views
#from mainapp import views
import os

urlpatterns = [
    path('',views.Index, name='Index'),
    path('register/',views.register),
    path('register/reg_done/',views.reg_done),
    path('login/',views.login),
    path('login/log_done/',views.log_done),
    path('student/', views.student, name="student"),
    path('reply/', views.reply, name="reply"),
    path('result/', views.result, name="result"),
    

] 