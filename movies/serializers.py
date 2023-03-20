from rest_framework import serializers
from .models import Movie, MovieOrder
from .models import Rantings


class MovieSerializer(serializers.Serializer):

    id = serializers.IntegerField(
        required=False, allow_null=True
        )
    title = serializers.CharField(
        max_length=127
        )
    duration = serializers.CharField(
        max_length=10, allow_null=True, default=None
        )
    rating = serializers.ChoiceField(
        choices=Rantings.choices, default=Rantings.G
        )
    synopsis = serializers.CharField(
        allow_null=True, default=None
        )
    added_by = serializers.SerializerMethodField()

    def create(self, validated_data):
        return Movie.objects.create(**validated_data)

    def get_added_by(self, obj):
        return obj.user.email


class MovieOrderSerializer(serializers.Serializer):
    buyed_at = serializers.DateTimeField(read_only=True)
    buyed_by = serializers.SerializerMethodField(read_only=True)
    id = serializers.IntegerField(read_only=True)
    title = serializers.SerializerMethodField(read_only=True)
    price = serializers.DecimalField(max_digits=8, decimal_places=2)

    def create(self, validated_data):
        return MovieOrder.objects.create(**validated_data)

    def get_title(self, obj):
        return obj.movie_order.title

    def get_buyed_by(self, obj):
        return obj.user_order.email
