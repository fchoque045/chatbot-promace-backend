from django.urls import path
from django.conf.urls import include
from rest_framework.routers import DefaultRouter
from .views import MessageViewSet, get_response

router = DefaultRouter()

router.register(r'messages',MessageViewSet,basename = 'messages')
router.register(r'get',get_response,basename = 'gets')

urlpatterns = [
    path(r'', include(router.urls)),
]