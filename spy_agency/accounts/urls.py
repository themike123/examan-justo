from django.urls import path
from django.contrib.auth.views import LogoutView
from . import views

urlpatterns =[
    path('', views.login, name='login'),
    path('register/', views.register, name='register'),
    path('logout/', LogoutView.as_view(), name='logout' ),
]