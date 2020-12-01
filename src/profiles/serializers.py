from rest_framework import serializers
from .models import UserNet


class GetUserNetSerializer(serializers.ModelSerializer):
    """вывод инфы о User"""
    avatar = serializers.ImageField(read_only=True)

    class Meta:
        model = UserNet
        exclude = (
            'password',
            'last_login',
            'is_active',
            'is_staff',
            'is_superuser',
            'user_permissions',
            'groups'
        )


class GetUserNetPublicSerializer(serializers.ModelSerializer):
    """вывод публичной инфы о User"""
    avatar = serializers.ImageField(read_only=True)

    class Meta:
        model = UserNet
        exclude = (
            'phone',
            'email',
            'password',
            'last_login',
            'is_active',
            'is_staff',
            'is_superuser',
            'user_permissions',
            'groups'
        )


class UserFollowerSerializer(serializers.ModelSerializer):
    """
    сериализация для подписчиков
    """
    avatar = serializers.ImageField(read_only=True)

    class Meta:
        model = UserNet
        fields = ('id', 'username', 'avatar')
