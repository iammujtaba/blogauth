from django.utils import timezone
from authservice.exceptions import RestValidationError
from authservice.models import User
from rest_framework import serializers
from django.contrib.auth import authenticate
from utils.validators import is_strong_password

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'email', 'first_name', 'last_name','email_verified_at','last_login','phone_number')


class UserRegistrationSerializer(UserSerializer):
    password = serializers.CharField(style={'input_type': 'password'}, write_only=True)
    confirm_password = serializers.CharField(style={'input_type': 'password'}, write_only=True)

    class Meta:
        model = User
        fields = ('email', 'first_name', 'last_name', 'phone_number', 'password', 'confirm_password')

    def validate(self, attrs):
        password = attrs['password']
        email = attrs['email']
        first_name = attrs.get('first_name')
        if password != attrs['confirm_password']:
            raise serializers.ValidationError({"password": "Password fields didn't match."})
        is_strong_password(password,raise_exception=True)
        if User.objects.filter(email=email).exists():
            raise serializers.ValidationError({"email": "Email is already taken."})
        if not first_name:
            raise serializers.ValidationError({"first_name": "First name is required."})
        return super().validate(attrs)

    def create(self, validated_data):
        validated_data.pop("confirm_password")
        print("validated data",validated_data)
        user = User.objects.create_user(**validated_data)
        print("user_created",user)
        print("marking email as verified")
        user.email_verified_at = timezone.now()
        user.save()
        return user

class UserLoginSerializer(serializers.Serializer):
    email = serializers.EmailField(required=True,style={"input":"text","placeholder":"Enter your email"})
    password = serializers.CharField(style={"input":"password","placeholder":"Enter your password here"})

    def get_user(self) -> User:
        kwargs = self.data
        super().validate(kwargs)
        email = kwargs["email"]
        password = kwargs["password"]
        user = authenticate(email=email,password=password)
        if not user: 
            raise RestValidationError("Wrong email/password.")
        return user
        