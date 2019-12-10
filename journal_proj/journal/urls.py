from django.urls import path
from . import views

urlpatterns = [
    path(r'', views.Reg.as_view()),
    path(r'auth/', views.Authoriz.as_view()),
    path(r'reg/', views.Reg.as_view()),
    path(r'main/', views.Main.as_view()),
    path(r'write/', views.Writing.as_view()),
    path(r'jour/', views.Read_jour.as_view()),
]