from django.urls import path
from django.contrib.auth.decorators import login_required

from . import views

urlpatterns =[
    path('', views.index, name='index'), 
    path('create/', views.new, name='new'), 
    path('<int:hit>/', views.show, name='show'), 
    path('bulk/', views.bulk, name='bulk'), 
]

#login_required(views.index)