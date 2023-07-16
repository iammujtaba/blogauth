from django.db import models
from authtoken.manager import AuthTokenManager
from utils.base_models import BaseModel
from django.utils import timezone

class AuthToken(BaseModel):
    user = models.ForeignKey('authservice.User', on_delete=models.CASCADE)
    access_token = models.CharField(max_length=255, unique=True)
    access_token_expires_at = models.DateTimeField()
    refresh_token = models.CharField(max_length=255, unique=True)
    refresh_token_expires_at = models.DateTimeField()
    ip_address = models.CharField(max_length=50, null=True, blank=True)
    user_agent = models.CharField(max_length=200, null=True, blank=True)
    city=models.TextField(null=True,blank=True)
    country=models.TextField(null=True,blank=True)
    device=models.CharField(max_length=100,null=True,blank=True)
    browser=models.CharField(max_length=100,null=True,blank=True)
    os=models.CharField(max_length=100,null=True,blank=True)

    objects = AuthTokenManager()

    def is_expired(self):
        return (
            self.access_token_expires_at <= timezone.now()
            or self.refresh_token_expires_at <= timezone.now()
        )

