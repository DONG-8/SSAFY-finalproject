from django.db import models
from django.conf import settings
from movies.models import Movie

# Create your models here.

# def community_image_path(instance, filename):
#     return f'user_{instance.pk}/{filename}'


class Community(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='user_community')
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='community')
    community_title = models.CharField(max_length=50)
    movie_title = models.CharField(max_length=50)
    content = models.TextField()
    poster_path = models.TextField()
    # image = models.ImageField(blank=True, upload_to='images/')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name="like_communities", blank=True, null=True)
    hate_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name="hate_communities", blank=True, null=True)


class Ceview(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='user_ceview')
    community = models.ForeignKey(Community, on_delete=models.CASCADE, related_name='ceview')
    rank = models.CharField(max_length=10)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name="like_ceviews", blank=True, null=True)
    hate_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name="hate_ceviews", blank=True, null=True)