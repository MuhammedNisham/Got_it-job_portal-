from django.urls import path
from .import views

urlpatterns = [
    path('community/', views.communityView, name='communitypage'),
    path('community/deletemessage/<int:message_id>/', views.deleteMessage, name='deletemessage'),
]