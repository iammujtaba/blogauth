from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework import viewsets,status
from authservice.serializer import UserRegistrationSerializer,UserSerializer,UserLoginSerializer
from authservice.models import User
from rest_framework.permissions import AllowAny
from authtoken.helpers import mark_access_token_expired_and_logout_user
from authtoken.serializer import AuthTokenSerializer

class UserActionViewSet(viewsets.GenericViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]

    @action(detail=False, methods=['post'],serializer_class=UserRegistrationSerializer)
    def register(self, request):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    @action(detail=False, methods=['post'],serializer_class=UserLoginSerializer)
    def login(self, request):
        # sourcery skip: assign-if-exp, reintroduce-else, remove-redundant-fstring, swap-if-expression
        serializer = self.get_serializer(data=request.data)
        if not serializer.is_valid():
            return Response(data = serializer.errors,status=status.HTTP_401_UNAUTHORIZED)
        authtoken = serializer.get_user()

        return Response(data=AuthTokenSerializer(authtoken).data,status=status.HTTP_200_OK)

    @action(detail=False, methods=['post'])
    def logout(self,request):
        mark_access_token_expired_and_logout_user(request)
        return Response(data={"message":"Logout successful.."},status=status.HTTP_200_OK)

