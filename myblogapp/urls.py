from django.urls import  path
from . import views

#registering our routes here....
urlpatterns = [
    path('', views.home)
]