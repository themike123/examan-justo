from django.urls import path
from django.contrib.auth.views import LogoutView
from . import views

app_name = 'hitman'

urlpatterns =[
    path('', views.index, name='index'),
    path('<int:hitman>/', views.show, name='show'),
]