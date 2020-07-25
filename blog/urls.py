"""blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render
from users import urls
def index(request):
    tem = loader.get_template('index.html')
    context = loader.render_to_string('index.html',{'name':'bob'},request)

    return HttpResponse(context)
    # return render(request,'index.html',{"name":"bob"})
urlpatterns = [
    path(r'admin/', admin.site.urls),
    path(r'index/',index),
    path(r'',index),
    path(r'user/',include('users.urls')),
    path(r'post/',include('post.urls'))
]
