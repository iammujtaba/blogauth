from rest_framework import serializers
from authtoken.models import AuthToken
from authservice.serializer import UserSerializer

class AuthTokenSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = AuthToken
        fields = ("access_token","refresh_token","access_token_expires_at","refresh_token_expires_at","user")