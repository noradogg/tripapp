from django.http import request
from django.urls import path, include
from django.views.generic import TemplateView
from django.shortcuts import redirect
from . import views

urlpatterns = [
    path('', include('allauth.urls')),
    path('', TemplateView.as_view(template_name = 'top.html'), name = 'top'),
    path('login/', TemplateView.as_view(template_name = 'register/login.html'), name='login'),
    path('logout/', views.Logout.as_view(), name='logout'),
    path('signup/', TemplateView.as_view(template_name = 'register/signup.html'), name='signup'),
    # path('test/', views.test(), name = 'test'),
]