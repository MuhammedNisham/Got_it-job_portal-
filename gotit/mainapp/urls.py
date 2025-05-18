from django.urls import path
from .import views

urlpatterns =[
    path('', views.homeView, name= 'homepage'),
    path('job', views.jobView, name='jobpage'),
    path('Profile', views.ProfileView, name='profilepage')
]