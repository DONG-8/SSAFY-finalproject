from rest_framework import serializers
from .models import Community, Ceview
from accounts.serializers import UserSerializer


class CommunitySerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    # image = serializers.ImageField(use_url=True)

    class Meta:
        model = Community
        fields = '__all__'


class CeviewSerializer(serializers.ModelSerializer):

    class Meta:
        model = Ceview
        fields = '__all__'