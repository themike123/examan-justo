from django.urls import path
from django.contrib.auth.views import LogoutView
from . import views

urlpatterns =[
    path('', views.index, name='index'),
    path('<int:hitmen>/', views.show, name='show'),
]