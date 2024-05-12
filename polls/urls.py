from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import *
from .views import MessageViewSet
from .views import EventsViewSet
from .views import UserApiViewSet
from .views import ProfileApiViewSet
from .views import TemplateViewSet




router = DefaultRouter()
router.register(r'user', UserApiViewSet)
router.register(r'events', EventsViewSet)
router.register(r'message', MessageViewSet)
router.register(r'profile', ProfileApiViewSet)
router.register(r'templates', TemplateViewSet)



urlpatterns = [
    # path('api/', UserProfileApi.as_view({'get': 'list', 'post': 'create'}), name='user_profiles_api'),
    path('', include(router.urls))
]