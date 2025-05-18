from django.shortcuts import render

from django.views.generic import CreateView
from django.urls import reverse_lazy
# importing custom form
from .forms import CustomLoginForm, CustomRegisterForm

from django.contrib.auth.views import LoginView
# Create your views here.

class UserSignUp(CreateView):
    form_class = CustomRegisterForm
    template_name = 'signup.html'
    success_url = reverse_lazy('login')

class UserLogin(LoginView):
    template_name = 'login.html'
    form_class = CustomLoginForm
