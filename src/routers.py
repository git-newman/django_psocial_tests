from django.urls import path, include
from .profiles import views
from rest_framework import permissions
from drf_yasg import openapi
from drf_yasg.views import get_schema_view

schema_view = get_schema_view(
    openapi.Info(
        title="Psocial",
        default_version='v1',
        description='Docs',
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('', include('src.profiles.urls')),
    path('swagger/', schema_view.with_ui()),
    path('wall/', include('src.wall.urls')),
]