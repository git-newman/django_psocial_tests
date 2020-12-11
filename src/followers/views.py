from django.core.exceptions import ObjectDoesNotExist
from rest_framework import generics, permissions, views, response
from .models import Follower
from .serializers import ListFollowerSerializer
from src.profiles.models import UserNet


class ListFollowerView(generics.ListAPIView):
    """
    вывод списка подписчиков пользователя
    """
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = ListFollowerSerializer

    def get_queryset(self):
        return Follower.objects.filter(user=self.request.user)


class FollowerView(views.APIView):
    """
    добавление себя в подписчики / удаление из подписчиков
    """
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, pk):
        try:
            user = UserNet.objects.get(id=pk)
        except ObjectDoesNotExist:
            return response.Response(status=404)

        Follower.objects.create(subscriber=request.user, user=user)
        return response.Response(status=201)

    def delete(self, request, pk):
        try:
            sub = Follower.objects.get(subscriber=request.user, user_id=pk)
        except ObjectDoesNotExist:
            return response.Response(status=404)
        sub.delete()
        return response.Response(status=204)
