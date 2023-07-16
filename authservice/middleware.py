from rest_framework import status,response
from authtoken.models import AuthToken
from django.http import JsonResponse

class AuthTokenValidator:
    '''
    Todo: Will think of moving this to auth-proxy/authtoken app as this is more related to authtoken and it's validation
    '''
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # sourcery skip: assign-if-exp, reintroduce-else, swap-if-expression
        is_valid,text = self.process_request(request)
        print("Token is valid?",is_valid,text)
        if not is_valid:
            return JsonResponse(data={"detail": text}, status=status.HTTP_401_UNAUTHORIZED)

        return self.get_response(request)

    def process_request(self, request):
        if self.should_validate_token(request):
            is_valid,text_msg = self.is_token_valid(request)
            if not is_valid:
                return is_valid, text_msg
        return True, None

    def should_validate_token(self, request):
        '''
        This will be replaced with auth-proxy app model which will act has gateway. It'll take care of all endpoints
        which url will require authorization and which will be open etc.
        '''
        return request.path.startswith('/auth/users/logout/')

    def is_token_valid(self, request):
        token = self.get_auth_token(request)
        if not token:
            return False, "authentication required to view this content."
        try:
            authtoken = AuthToken.objects.get(access_token=token)
        except AuthToken.DoesNotExist as e:
            return False, "authentication required passed to view this content is invalid."

        if authtoken.is_expired():
            return False, "authorization token has expired, please login again"


        user = authtoken.user
        print(f"user found for token {token} with email {user.email}")
        request._user = user # can't use request.user as getting CSRF Failed: CSRF cookie not set. # Will check this later
        request.access_token = token
        return True, None

    def get_auth_token(self, request):
        return request.META.get('HTTP_AUTHORIZATION')

    def create_response(self, data, status):
        from rest_framework.response import Response
        return Response(data, status=status)