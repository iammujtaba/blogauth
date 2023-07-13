from rest_framework import routers
from authservice.views import UserActionViewSet
from django.conf.urls import include
from django.urls.conf import path


router = routers.DefaultRouter()
router.register(r'users', UserActionViewSet)

urlpatterns = [
    path('', include(router.urls)),
]