from rest_framework import routers
from authservice.views import UserViewSet
from django.conf.urls import include
from django.urls.conf import path




router = routers.DefaultRouter()
router.register(r'users', UserViewSet)

urlpatterns = [
    path('', include(router.urls)),
]