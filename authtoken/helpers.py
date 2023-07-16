from django.contrib.auth import logout
from authtoken.models import AuthToken
from django.utils import timezone
from django.http import HttpRequest

def mark_access_token_expired_and_logout_user(request: HttpRequest) -> AuthToken:
    access_token = request.access_token
    logout(request) # since we are using django authenticate while login hence we've do logout.
    authtoken = AuthToken.objects.get(access_token=access_token)
    authtoken.access_token_expires_at = timezone.now()
    authtoken.refresh_token_expires_at = timezone.now()
    authtoken.save()
    return authtoken

