from django.urls import path
from .import views 
from .views import ProfileView

urlpatterns =[
    path('', views.homeView, name= 'homepage'),
    path('Profile/', views.ProfileView, name='profilepage'),
    path('profile/edit/', views.edit_profile, name='editprofile')
]