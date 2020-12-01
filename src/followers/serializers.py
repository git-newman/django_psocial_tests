from rest_framework import serializers
from .models import Follower
from src.profiles.serializers import UserFollowerSerializer


class ListFollowerSerializer(serializers.ModelSerializer):

    subscriber = UserFollowerSerializer(read_only=True)

    class Meta:
        model = Follower
        fields = ('subscriber',)

