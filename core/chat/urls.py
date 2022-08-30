from django.urls import path
from django.views.generic import TemplateView
from .views import MessageListAPIView, MessageTypeListAPIView

urlpatterns = [
    path('',TemplateView.as_view(template_name="index.html"), name = 'index'),
    # path('response/',get_response, name = 'get_resonse'),
    # path('messages/', MessageViewSet.as_view(), name='message'),
    path('messages/bienvenida', MessageListAPIView.as_view(), name='message_list'),
    path('messages/type', MessageTypeListAPIView.as_view(), name='message_type_list')
]
