from rest_framework import serializers
from .models import Artist, Album, Song, AlbumSong


class SongSerializer(serializers.ModelSerializer):
    """Сериализатор для песни"""

    class Meta:
        model = Song
        fields = ['id', 'name']


class AlbumSongSerializer(serializers.ModelSerializer):
    """Сериализатор для связи альбом-песня"""
    song = SongSerializer(read_only=True)

    class Meta:
        model = AlbumSong
        fields = ['song', 'track_number']


class AlbumSerializer(serializers.ModelSerializer):
    """Сериализатор для альбома"""
    artist_name = serializers.CharField(source='artist.name', read_only=True)
    songs = AlbumSongSerializer(source='album_songs', many=True, read_only=True)

    class Meta:
        model = Album
        fields = ['id', 'artist', 'artist_name', 'release_year', 'songs']


class ArtistSerializer(serializers.ModelSerializer):
    """Сериализатор для исполнителя"""

    class Meta:
        model = Artist
        fields = ['id', 'name']