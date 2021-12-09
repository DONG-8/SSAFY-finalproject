from rest_framework import serializers, status
from rest_framework import permissions
from rest_framework.response import Response
from django.http import JsonResponse
from rest_framework.decorators import api_view, permission_classes

from django.shortcuts import get_object_or_404

from rest_framework.permissions import AllowAny, IsAuthenticated
from accounts.models import User
from .models import Community, Ceview
from .serializers import CommunitySerializer, CeviewSerializer

@api_view(['GET'])
def community_list(request):
    community_li = Community.objects.all()
    serializer = CommunitySerializer(community_li, many=True)
    return Response(serializer.data)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def community_create(request):
    serializer = CommunitySerializer(data=request.data)

    if serializer.is_valid(raise_exception=True):
        serializer.save(user=request.user)
        return Response(serializer.data)


@api_view(['GET'])
def community_detail(request, community_id):
    community = get_object_or_404(Community, pk=community_id)
    serializer = CommunitySerializer(community)
    return Response(serializer.data)


@api_view(['DELETE'])
def community_delete(request, user_pk, community_id):
    user = get_object_or_404(User, pk=user_pk)
    if request.user == user:
        community = get_object_or_404(Community, pk=community_id)
        community.delete()
        return Response('DELETE SUCCESS')


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def community_update(request, community_id):
    # print(request.)
    # user = get_object_or_404(User, pk=request.user)
    # if request.user == user:
    community = get_object_or_404(Community, pk=community_id)
    serializer = CommunitySerializer(instance=community, data=request.data)

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    else:
        return Response(False)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def community_like(request, community_id):
    community = get_object_or_404(Community, pk=community_id)
    user = request.user
    if community.like_users.filter(pk=user.pk).exists():
        community.like_users.remove(user)
        like = False
    else:
        community.like_users.add(user)
        like = True
    like_status = {
        'like': like,
        'count': community.like_users.count(),
    }
    return JsonResponse(like_status)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def community_hate(request, community_id):
    community = get_object_or_404(Community, pk=community_id)
    user = request.user
    if community.hate_users.filter(pk=user.pk).exists():
        community.hate_users.remove(user)
        hate = False
    else:
        community.hate_users.add(user)
        hate = True
    hate_status = {
        'hate': hate,
        'count': community.hate_users.count(),
    }
    return JsonResponse(hate_status)


@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def review_list_create(request, community_id):
    if request.method == 'GET':
        reviews = Ceview.objects.filter(community=community_id)
        serializer = CeviewSerializer(reviews, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        community = get_object_or_404(Community, pk=community_id)
        serializer = CeviewSerializer(data=request.data)

        if serializer.is_valid(raise_exception=True):
            serializer.community = community
            serializer.user = request.user
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def community_review_update(request, community_id, review_pk):
    community = get_object_or_404(Community, pk=community_id)
    ceview = get_object_or_404(Ceview, pk=review_pk)
    serializer = CeviewSerializer(instance=ceview, data=request.data)

    if serializer.is_valid():
        serializer.community = community
        serializer.save()
        return Response(serializer.data)
    else:
        return Response(False)


@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def community_review_delete(request, community_id, review_pk):
    ceview = get_object_or_404(Ceview, pk=review_pk)
    ceview.delete()
    return Response('DELETE SUCCESS!')


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def community_review_like(request, community_id, review_pk):
    ceview = get_object_or_404(Ceview, pk=review_pk)
    user = request.user
    if ceview.like_users.filter(pk=user.pk).exists():
        ceview.like_users.remove(user)
        like = False
    else:
        ceview.like_users.add(user)
        like = True
    like_status = {
        'like': like,
        'count': ceview.like_users.count(),
    }
    return JsonResponse(like_status)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def community_review_hate(request, community_id, review_pk):
    ceview = get_object_or_404(Ceview, pk=review_pk)
    user = request.user
    if ceview.hate_users.filter(pk=user.pk).exists():
        ceview.hate_users.remove(user)
        hate = False
    else:
        ceview.hate_users.add(user)
        hate = True
    hate_status = {
        'hate': hate,
        'count': ceview.hate_users.count(),
    }
    return JsonResponse(hate_status)