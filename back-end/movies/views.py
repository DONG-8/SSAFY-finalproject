from rest_framework import serializers, status
from rest_framework import permissions
from rest_framework.response import Response
from django.http import JsonResponse
from rest_framework.decorators import api_view, permission_classes

from django.shortcuts import get_object_or_404

from rest_framework.permissions import AllowAny, IsAuthenticated

from .serializers import MovieSerializer, ReviewSerializer, GenreSerializer
from .models import Movie, Review, Genre

@api_view(['GET'])
def movie_all(request):
    movies = Movie.objects.all()
    serializer = MovieSerializer(movies, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def movie_list(request):
    movies = Movie.objects.all().order_by('-id')[723:]
    # movies = request.user.movie_set.all()
    serializer = MovieSerializer(movies, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def movie_list_recent(request):
    movies_recent = Movie.objects.all().order_by('-id')[703:723]
    # movies = request.user.movie_set.all()
    serializer = MovieSerializer(movies_recent, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def movie_detail(request, movie_id):
    movie = Movie.objects.get(pk=movie_id)
    serializer = MovieSerializer(movie)

    # 같은 장르의 영화 최신순 10개 받아오기
    genre = movie.genre.all().values_list('id', flat=True)
    similar_movies = Movie.objects.filter(genre__id__in=genre).prefetch_related('genre').distinct()[:8]
    
    similar_serializer = MovieSerializer(similar_movies, many=True)
    context = {
        "movie": serializer.data,
        "similar_movies": similar_serializer.data,
    }
    return Response(context)


@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def movie_like(request, movie_id):
    movie = get_object_or_404(Movie, pk=movie_id)
    user = request.user
    if movie.like_users.filter(pk=user.pk).exists():
        movie.like_users.remove(user)
        like = False
    else:
        movie.like_users.add(user)
        like = True
    like_status = {
        'like': like,
        'count': movie.like_users.count(),
    }
    return JsonResponse(like_status)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def movie_hate(request, movie_id):
    movie = get_object_or_404(Movie, pk=movie_id)
    user = request.user
    if movie.hate_users.filter(pk=user.pk).exists():
        movie.hate_users.remove(user)
        hate = False
    else:
        movie.hate_users.add(user)
        hate = True
    hate_status = {
        'hate': hate,
        'count': movie.hate_users.count(),
    }
    return JsonResponse(hate_status)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def movie_favorite(request, movie_id):
    movie = get_object_or_404(Movie, pk=movie_id)
    user = request.user
    if movie.favorite_users.filter(pk=user.pk).exists():
        movie.favorite_users.remove(user)
        favorite = False
    else:
        movie.favorite_users.add(user)
        favorite = True
    favorite_status = {
        'favorite': favorite,
        'count': movie.favorite_users.count(),
    }
    return JsonResponse(favorite_status)



@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def review_list_create(request, movie_id):
    if request.method == 'GET':
        reviews = Review.objects.filter(movie=movie_id)
        serializer = ReviewSerializer(reviews, many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        movie = get_object_or_404(Movie, pk=movie_id)
        serializer = ReviewSerializer(data=request.data)

        if serializer.is_valid(raise_exception=True):
            serializer.movie = movie
            serializer.user = request.user
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)


# @api_view(['GET'])
# # @permission_classes([IsAuthenticated])
# def movie_review(request):
#     reviews = Review.objects.all()
#     serializer = ReviewSerializer(reviews, many=False)
#     return Response(serializer.data)


# @api_view(['POST'])
# @permission_classes([IsAuthenticated])
# def movie_review_create(request, movie_id):
#     movie = get_object_or_404(Movie, pk=movie_id)
#     serializer = ReviewSerializer(data=request.data)

#     if serializer.is_valid(raise_exception=True):
#         serializer.movie = movie
#         serializer.save(user=request.user)
#         return Response(serializer.data)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def movie_review_update(request, movie_id, review_pk):
    movie = get_object_or_404(Movie, pk=movie_id)
    review = get_object_or_404(Review, pk=review_pk)
    serializer = ReviewSerializer(instance=review, data=request.data)

    if serializer.is_valid():
        serializer.movie = movie
        serializer.save()
        return Response(serializer.data)
    else:
        return Response(False)


@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def movie_review_delete(request, movie_id, review_pk):
    review = get_object_or_404(Review, pk=review_pk)
    review.delete()
    return Response('DELETE SUCCESS!')



@api_view(['POST'])
@permission_classes([IsAuthenticated])
def movie_review_like(request, movie_id, review_pk):
    review = get_object_or_404(Review, pk=review_pk)
    user = request.user
    if review.like_users.filter(pk=user.pk).exists():
        review.like_users.remove(user)
        like = False
    else:
        review.like_users.add(user)
        like = True
    like_status = {
        'like': like,
        'count': review.like_users.count(),
    }
    return JsonResponse(like_status)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def movie_review_hate(request, movie_id, review_pk):
    review = get_object_or_404(Review, pk=review_pk)
    user = request.user
    if review.hate_users.filter(pk=user.pk).exists():
        review.hate_users.remove(user)
        hate = False
    else:
        review.hate_users.add(user)
        hate = True
    hate_status = {
        'hate': hate,
        'count': review.hate_users.count(),
    }
    return JsonResponse(hate_status)



@api_view(['GET'])
def genre_list(request):
    genres = Genre.objects.all()
    serializer = GenreSerializer(genres, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def movie_by_genre(request):
    horror_movies = Movie.objects.filter(genre=0)[:20]
    sf_movies = Movie.objects.filter(genre=1)[:20]
    criminal_movies = Movie.objects.filter(genre=2)[:20]
    mystery_movies = Movie.objects.filter(genre=3)[:20]
    thriller_movies = Movie.objects.filter(genre=4)[:20]
    romance_movies = Movie.objects.filter(genre=5)[:20]
    fantasy_movies = Movie.objects.filter(genre=6)[:20]
    war_movies = Movie.objects.filter(genre=7)[:20]
    animation_movies = Movie.objects.filter(genre=8)[:20]
    adventure_movies = Movie.objects.filter(genre=9)[:20]
    documentary_movies = Movie.objects.filter(genre=10)[:20]
    action_movies  = Movie.objects.filter(genre=11)[:20]
    drama_movies = Movie.objects.filter(genre=12)[:20]
    suspense_movies = Movie.objects.filter(genre=13)[:20]
    comedy_movies = Movie.objects.filter(genre=14)[:20]
    family_movies = Movie.objects.filter(genre=15)[:20]
    concert_movies = Movie.objects.filter(genre=16)[:20]
    musical_movies = Movie.objects.filter(genre=17)[:20]
    
    horror_serializer = MovieSerializer(horror_movies, many=True)
    sf_serializer = MovieSerializer(sf_movies, many=True)
    criminal_serializer = MovieSerializer(criminal_movies, many=True)
    mystery_serializer = MovieSerializer(mystery_movies, many=True)
    thriller_serializer = MovieSerializer(thriller_movies, many=True)
    romance_serializer = MovieSerializer(romance_movies, many=True)
    fantasy_serializer = MovieSerializer(fantasy_movies, many=True)
    war_serializer = MovieSerializer(war_movies, many=True)
    animation_serializer = MovieSerializer(animation_movies, many=True)
    adventure_serializer = MovieSerializer(adventure_movies, many=True)
    documentary_serializer = MovieSerializer(documentary_movies, many=True)
    action_serializer = MovieSerializer(action_movies, many=True)
    drama_serializer = MovieSerializer(drama_movies, many=True)
    suspense_serializer = MovieSerializer(suspense_movies, many=True)
    comedy_serializer = MovieSerializer(comedy_movies, many=True)
    family_serializer = MovieSerializer(family_movies, many=True)
    concert_serializer = MovieSerializer(concert_movies, many=True)
    musical_serializer = MovieSerializer(musical_movies, many=True)
    context = {
        'horrorMovies': horror_serializer.data,
        'sfMovies': sf_serializer.data,
        'criminalMovies': criminal_serializer.data,
        'mysteryMovies': mystery_serializer.data,
        'thrillerMovies': thriller_serializer.data,
        'romanceMovies': romance_serializer.data,
        'fantasyMovies': fantasy_serializer.data,
        'warMovies': war_serializer.data,
        'animationMovies': animation_serializer.data,
        'adventureMovies': adventure_serializer.data,
        'documentaryMovies': documentary_serializer.data,
        'actionMovies': action_serializer.data,
        'dramaMovies': drama_serializer.data,
        'suspenseMovies': suspense_serializer.data,
        'comedyMovies': comedy_serializer.data,
        'familyMovies': family_serializer.data,
        'concertMovies': concert_serializer.data,
        'musicalMovies': musical_serializer.data,
    }
    return Response(context)


api_view(['GET'])
def movie_by_grade(request):
    movies_all = Movie.objects.filter(grade=0)[:20]
    movies_12 = Movie.objects.filter(grade=1)[:20]
    movies_15 = Movie.objects.filter(grade=2)[:20]
    movies_19 = Movie.objects.filter(grade=3)[:20]

    serializer_all = MovieSerializer(movies_all, many=True)
    serializer_12 = MovieSerializer(movies_12, many=True)
    serializer_15 = MovieSerializer(movies_15, many=True)
    serializer_19 = MovieSerializer(movies_19, many=True)

    context = {
        'allMovies': serializer_all.data,
        '12Movies': serializer_12.data,
        '15Movies': serializer_15.data,
        '19Movies': serializer_19.data,
    }
    return Response(context)