from django.db import models
from django.conf import settings

# Create your models here.
class Genre(models.Model):
    name = models.CharField(max_length=20)

class Grade(models.Model):
    rating = models.CharField(max_length=20)

class Movie(models.Model):
    id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=50)
    vote = models.FloatField()
    country = models.CharField(max_length=50)
    time = models.CharField(max_length=10)
    grade = models.ManyToManyField(Grade, related_name='movie_grade')
    poster_path = models.TextField()
    actor_1 = models.CharField(max_length=20)
    actor_2 = models.CharField(max_length=20, default='')
    actor_3 = models.CharField(max_length=20, default='')
    year = models.IntegerField()
    month = models.IntegerField()
    day = models.IntegerField(default='')
    content = models.TextField()
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name="like_movies")
    hate_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name="hate_movies")
    favorite_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name="favorite_movies")
    genre = models.ManyToManyField(Genre, related_name='movie_genre')

    def __str__(self):
        return self.title

class Review(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='user_review')
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='review')
    rank = models.CharField(max_length=10)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name="like_reviews", blank=True, null=True)
    hate_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name="hate_reviews", blank=True, null=True)