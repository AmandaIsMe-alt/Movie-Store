from rest_framework.views import APIView, Response, status
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404
from .serializers import UserSerializer
from .models import User
from .permissions import PermissionsPersonalized


class UserView(APIView):

    def post(self, request):
        new_user = UserSerializer(data=request.data)
        new_user.is_valid(raise_exception=True)
        new_user.save()

        return Response(new_user.data, status.HTTP_201_CREATED)


class UserDetailView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [PermissionsPersonalized, IsAuthenticated]

    def get(self, request, user_id):
        user_list = User.objects.get(id=user_id)
        self.check_object_permissions(request, user_list)
        serializer = UserSerializer(user_list)
        return Response(serializer.data, status.HTTP_200_OK)

    def patch(self, request, user_id):
        user_found = get_object_or_404(User, id=user_id)
        self.check_object_permissions(request, user_found)

        serializer = UserSerializer(
            user_found, data=request.data, partial=True
            )
        serializer.is_valid(raise_exception=True)

        serializer.save()

        return Response(serializer.data, status.HTTP_200_OK)


class LoginTokenJWTView(TokenObtainPairView):
    ...
