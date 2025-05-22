from django.urls import path
from . import views

urlpatterns = [
    path('apply/<int:job_id>/', views.applyView, name='applypage'),
]