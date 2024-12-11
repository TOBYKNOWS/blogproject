from django.urls import  path
from . import views

#registering our routes here....
urlpatterns = [
    path('', views.home),
    path('/footer.html/', views.footer),
    
    path('form.html/', views.form),
    path('blogform.html/', views.blogform)
# path('font.html/', views.font),

]


