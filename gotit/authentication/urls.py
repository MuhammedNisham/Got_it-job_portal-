from django.urls import path

from .views import UserSignUp, UserLogin

urlpatterns = [
    path('login', UserLogin.as_view(), name='login'),
    path('signup', UserSignUp.as_view(), name='signup')
]