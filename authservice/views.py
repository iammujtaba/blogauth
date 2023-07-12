from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework import viewsets,mixins,generics,status
from authservice.serializer import UserRegistrationSerializer,UserSerializer
from authservice.models import User
from rest_framework.permissions import IsAuthenticated,AllowAny


class UserViewSet(mixins.CreateModelMixin,mixins.DestroyModelMixin,mixins.ListModelMixin,mixins.RetrieveModelMixin,viewsets.GenericViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer



    @action(detail=False, methods=['post'],url_path='register',serializer_class=UserRegistrationSerializer,permission_classes=[AllowAny])
    def register(self, request):
        serializer = UserRegistrationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    @action(detail=False, methods=['post'],url_path='delete')
    def delete(self, request):
        user = request.user
        if not user:
            return Response({"message": "User not found"},status=status.HTTP_404_NOT_FOUND)
        print(user.id)
        return Response({"message": "kuch nai mila.."},status=status.HTTP_404_NOT_FOUND)