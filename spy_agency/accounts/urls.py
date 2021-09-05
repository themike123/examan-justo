from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from . import views

urlpatterns =[
    path('', LoginView.as_view(template_name='accounts/login.html'), name='login'),    
    path('register/', views.register, name='register'),
    path('logout/', LogoutView.as_view(), name='logout' ),
]