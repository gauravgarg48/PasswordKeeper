from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register),
    path('signin/', views.signin),
    # path('', views.index, name='index'),
    path('signout/', views.signout),
    path('homepage/', views.home, name ='home'),
]