from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

# router для автоматической генерации URLs
router = DefaultRouter()
router.register(r'artists', views.ArtistViewSet, basename='artist')
router.register(r'albums', views.AlbumViewSet, basename='album')
router.register(r'songs', views.SongViewSet, basename='song')

urlpatterns = [
    path('', include(router.urls)),
]