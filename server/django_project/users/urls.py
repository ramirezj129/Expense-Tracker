
from django.contrib import admin
from django.urls import path
from users.views import UserRegistrationView, UserLoginView



urlpatterns = [

    path('register/', UserRegistrationView.as_view(), name='user-registration'),
    path('login/', UserLoginView.as_view(), name='user-login'),


]