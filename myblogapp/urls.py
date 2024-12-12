from django.urls import  path
from . import views

#registering our routes here....
urlpatterns = [
    path('', views.home),
    path('footer/', views.footer),
    
    path('form/', views.form),
    path('blog/', views.blogform),
    path('contact/', views.contactpage)
# path('font.html/', views.font)

]


