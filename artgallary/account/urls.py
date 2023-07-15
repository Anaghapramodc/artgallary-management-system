from django.contrib import admin
from django.urls import path, include, re_path
from django.contrib.auth import views as auth_views

from .views import SignUpView, Logout, Login

urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
    path('login/', auth_views.LoginView.as_view(), name="login"),
    path('Logout/', Logout.as_view(), name='logout-page'),

]