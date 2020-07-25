from django.urls import path
from django.shortcuts import render
from django.http import JsonResponse
from .views import reg,login
urlpatterns = [
    path(r'reg',reg),
    path(r'login',login)
]