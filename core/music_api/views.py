from rest_framework import viewsets, generics, filters
from django_filters.rest_framework import DjangoFilterBackend
from .models import Artist, Album, Song, AlbumSong
from .serializers import (
    ArtistSerializer, AlbumSerializer, SongSerializer,
    AlbumSongSerializer
)


class ArtistViewSet(viewsets.ModelViewSet):
    """ViewSet для исполнителей"""
    queryset = Artist.objects.all().prefetch_related('albums__album_songs__song')
    serializer_class = ArtistSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['name']
    ordering_fields = ['name']
    ordering = ['name']


class AlbumViewSet(viewsets.ModelViewSet):
    """ViewSet для альбомов"""
    queryset = Album.objects.all().select_related('artist').prefetch_related('album_songs__song')
    serializer_class = AlbumSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['artist', 'release_year']
    search_fields = ['artist__name']
    ordering_fields = ['release_year', 'artist__name']
    ordering = ['-release_year']


class SongViewSet(viewsets.ModelViewSet):
    """ViewSet для песен"""
    queryset = Song.objects.all().prefetch_related('song_albums__album__artist')
    serializer_class = SongSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['name']
    ordering_fields = ['name']
    ordering = ['name']

