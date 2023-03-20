from .permissions import IsEmployee
from django.shortcuts import get_object_or_404
from rest_framework.pagination import PageNumberPagination
from rest_framework.views import APIView, Response, status
from .models import Movie
from .serializers import MovieSerializer, MovieOrderSerializer
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated


class MovieView(APIView, PageNumberPagination):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsEmployee]

    def post(self, request):
        new_movie = MovieSerializer(data=request.data)
        new_movie.is_valid(raise_exception=True)
        new_movie.save(user=request.user)
        return Response(new_movie.data, status.HTTP_201_CREATED)

    def get(self, request):
        movies_list = Movie.objects.all()
        result = self.paginate_queryset(movies_list, request, self)
        serializer = MovieSerializer(result, many=True)
        return self.get_paginated_response(serializer.data)


class MovieOrderView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request, movie_id):
        movie_list = get_object_or_404(Movie, id=movie_id)
        movie = MovieOrderSerializer(data=request.data)
        movie.is_valid(raise_exception=True)
        movie.save(user_order=request.user, movie_order=movie_list)
        return Response(movie.data, status.HTTP_201_CREATED)


class MovieDetailView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsEmployee]

    def get(self, request, movie_id):
        movie_list = get_object_or_404(Movie, id=movie_id)
        serializer = MovieSerializer(movie_list)
        return Response(serializer.data, status.HTTP_200_OK)

    def delete(self, request, movie_id):
        movie = get_object_or_404(Movie, id=movie_id)
        movie.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
