from django.urls import path
from . import views

urlpatterns = [
    path('apply/<int:job_id>/', views.applyView, name='applypage'),
    path('activity/', views.activityView, name='activitypage'),
    path('activity/applied', views.appliedView, name='appliedpage')
]