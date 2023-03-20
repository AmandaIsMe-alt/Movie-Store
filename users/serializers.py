from rest_framework import serializers
from .models import User
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer


class UserSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)

    email = serializers.EmailField(max_length=127)
    def validate_email(self, email):
        email_already_exists = User.objects.filter(email=email).exists()
        if email_already_exists:
            raise serializers.ValidationError(
                detail="email already registered."
                )
        return email

    password = serializers.CharField(write_only=True)
    is_employee = serializers.BooleanField(allow_null=True, default=False)
    is_superuser = serializers.BooleanField(read_only=True)
    first_name = serializers.CharField(max_length=50)
    last_name = serializers.CharField(max_length=50)
    birthdate = serializers.DateField(allow_null=True, default=None)
    
    username = serializers.CharField(max_length=20)
    def validate_username(self, username):
        username_already_exists = User.objects.filter(
            username=username
            ).exists()

        if username_already_exists:
            raise serializers.ValidationError(detail="username already taken.")
        return username

    def create(self, validated_data):
        if not validated_data["is_employee"]:
            user = User.objects.create_user(**validated_data)
            return user
        user = User.objects.create_superuser(**validated_data)

        return user

    def update(self, instance, validated_data):
        for key, value in validated_data.items():
            setattr(instance, key, value)

        instance.set_password(raw_password=instance.password)

        instance.save()

        return instance


class UserJWTSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        token["is_superuser"] = user.is_superuser

        return token
