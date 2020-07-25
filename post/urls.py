from django.urls import path
from .views import pub,get,getall
urlpatterns = [
    path(r'pub',pub),
    path(r'<int:id>',get),
    path(r'',getall)
]