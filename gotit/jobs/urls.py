from django.urls import path
from .import views

urlpatterns = [
    path('jobs/', views.jobView, name='jobpage'),
    path('jobs/addjob/', views.addJobView, name='addjobpage'),
    path('jobs/edit/<int:job_id>', views.editJobView, name='editjobpage'),
    path('jobs/delete/<int:job_id>/', views.deleteJobView, name='deletejobpage'),
]