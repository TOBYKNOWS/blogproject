from django.urls import  path
from . import views

#registering our routes here....
urlpatterns = [
    path('', views.home),
    # path('/footer.html/', views.footer)
    # path('font.html/', views.font),
    path('form.html/', views.form)
]