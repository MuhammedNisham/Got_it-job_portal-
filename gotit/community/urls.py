from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from .import views

urlpatterns = [
    path('community/', views.communityView, name='communitypage'),
    path('community/deletemessage/<int:message_id>/', views.deleteMessage, name='deletemessage'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)