import requests, re, random

from django.shortcuts import get_object_or_404, render
from django.contrib.auth import get_user_model
from rest_framework import permissions
from rest_framework.decorators import api_view
from rest_framework.viewsets import ReadOnlyModelViewSet
from rest_framework import serializers, status
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated

from movies.models import Movie
from accounts.models import User
from community.models import Community
from movies.serializers import MovieSerializer, MovieListSerializer
from accounts.serializers import UserSerializer
from django.db.models import Count

from urllib.parse import quote_plus
from bs4 import BeautifulSoup
from selenium import webdriver

# Create your views here.

class MovieListViewSet(ReadOnlyModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieListSerializer

class MovieRecommendByDayViewSet(ReadOnlyModelViewSet):
    def week():
        base_url = 'https://www.google.com/search?q='
        plus_url = quote_plus('오늘의 요일')
        url = base_url + plus_url
        driver = webdriver.Chrome(executable_path='C:\\Users\\analysis\\Desktop\\SSAFY\\projects\\A_projects\\finalproject\\back-end\\chromedriver.exe')
        driver.get(url)
        html = driver.page_source
        soup = BeautifulSoup(html)
        week = soup.select_one('#rso > div.ULSxyf > div > div > div.vk_gy.vk_sh.card-section.sL6Rbf > div.vk_bk.dDoNo.FzvWSb').text
        if re.search(r'월요일', week):
            genre_by_week = [1,13]
        elif re.search(r'화요일', week):
            genre_by_week = [7,9,11]
        elif re.search(r'수요일', week):
            genre_by_week = [5,10,12,15]
        elif re.search(r'목요일', week):
            genre_by_week = [6,8,14]
        elif re.search(r'금요일', week):
            genre_by_week = [0,4]
        elif re.search(r'토요일', week):
            genre_by_week = [16,17]
        else:
            genre_by_week = [2,3]

        return Movie.objects.filter(genre__in=genre_by_week)
    queryset = week()
    serializer_class = MovieListSerializer



@api_view(['GET'])
def today_user_list(request):
    community = Community.objects.values('user_id').annotate(num_user=Count('user_id')).order_by('-num_user')[:10]
    print(community)
    person = random.choice(community)
    person_id = [person['user_id']]
    user = get_object_or_404(User, pk=person_id[0])
    print(person_id[0])
    userserializer = UserSerializer(user)
    movies = Movie.objects.filter(like_users__in = person_id)
    print(movies)
    serializer = MovieSerializer(movies, many=True)

    context = {
        'user': userserializer.data,
        'movies': serializer.data,
    }
    return Response(context)


@api_view(['GET'])
def movie_in_korea(request):
    komovies = Movie.objects.filter(country = '한국').order_by('-vote')
    serializer = MovieSerializer(komovies, many=True)
    return Response(serializer.data)