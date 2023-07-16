from django.db import models
from utils.futils import generate_access_refresh_token
from django.utils import timezone
from datetime import timedelta
from django.conf import settings

class AuthTokenManager(models.Manager):

    def create_token(self,user):
        access_token, refresh_token = generate_access_refresh_token()
        return self.create(
            access_token = access_token,
            refresh_token = refresh_token,
            access_token_expires_at = timezone.now() + timedelta(seconds=settings.ACCESS_TOKEN_TIMEOUT),
            refresh_token_expires_at = timezone.now() + timedelta(seconds=settings.REFRESH_TOKEN_TIMEOUT),
            user = user
        )