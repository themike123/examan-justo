from django.urls import path
from . import views

app_name = 'hits'


urlpatterns =[
    path('', views.index, name='index'), 
    path('create/', views.new, name='new'), 
    path('<int:hit>/', views.show, name='show'), 
    path('bulk/', views.bulk, name='bulk'), 
]