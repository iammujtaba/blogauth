from rest_framework import status
from authservice.models import User


class AuthTokenValidator:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        self.process_request(request)
        return self.get_response(request)

    def process_request(self, request):
        if self.should_validate_token(request):
            valid = self.is_token_valid(request)
            if not valid:
                response_data = {"detail": "Invalid token."}
                return self.create_response(response_data, status=status.HTTP_401_UNAUTHORIZED)

    def should_validate_token(self, request):
        return request.path.startswith('/auth/')

    def is_token_valid(self, request):
        token = self.get_auth_token(request)
        print("received token is ",token)
        if not token:
            print("token not found")
            return False
        if User.objects.filter(email=token).exists():
            request.user = User.objects.get(email=token)
            return True

    def get_auth_token(self, request):
        return request.META.get('HTTP_AUTHORIZATION')

    def create_response(self, data, status):
        from rest_framework.response import Response
        return Response(data, status=status)