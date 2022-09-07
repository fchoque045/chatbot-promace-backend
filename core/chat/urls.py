from django.urls import path
from django.views.generic import TemplateView
from .views import GenericoListAPIView, CategoriaListAPIView, PreguntaListAPIView

urlpatterns = [
    path('',TemplateView.as_view(template_name="index.html"), name = 'index'),
    # path('response/',get_response, name = 'get_resonse'),
    # path('messages/', MessageViewSet.as_view(), name='message'),
    path('generico/', GenericoListAPIView.as_view(), name='generico_list'),
    path('categoria/', CategoriaListAPIView.as_view(), name='categoria_list'),
    path('pregunta/', PreguntaListAPIView.as_view(), name='pregunta_list'),
]
