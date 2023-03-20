from django.db import models


class Rantings(models.TextChoices):
    G = "G"
    PG13 = "PG-13"
    NC17 = "NC-17"
    PG = "PG"
    R = "R"


class Movie(models.Model):
    title = models.CharField(
        max_length=127
        )
    user = models.ForeignKey(
        "users.User", on_delete=models.CASCADE, related_name="movies"
        )
    duration = models.CharField(
        max_length=10, null=True, default=None
        )
    rating = models.CharField(
        max_length=20, choices=Rantings.choices,
        default=Rantings.G, null=True
        )
    synopsis = models.TextField(
        null=True, default=None
        )   


class MovieOrder(models.Model):
    buyed_at = models.DateTimeField(
        auto_now_add=True
        )
    price = models.DecimalField(
        max_digits=8, decimal_places=2
        )
    movie_order = models.ForeignKey(
        "movies.Movie", on_delete=models.CASCADE,
        )
    user_order = models.ForeignKey(
        "users.User", on_delete=models.CASCADE,
        )
