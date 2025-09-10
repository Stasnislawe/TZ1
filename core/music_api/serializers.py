from rest_framework import serializers
from .models import Artist, Album, Song, AlbumSong


class SongSerializer(serializers.ModelSerializer):
    """Сериализатор для песни"""

    class Meta:
        model = Song
        fields = ['id', 'name']


class AlbumSongCreateSerializer(serializers.ModelSerializer):
    """Сериализатор для создания связи альбом-песня"""

    class Meta:
        model = AlbumSong
        fields = ['album', 'song', 'track_number']


class AlbumSongSerializer(serializers.ModelSerializer):
    """Сериализатор для отображения связи альбом-песня"""
    song_name = serializers.CharField(source='song.name', read_only=True)
    album_info = serializers.CharField(source='album.__str__', read_only=True)
    artist_name = serializers.CharField(source='album.artist.name', read_only=True)

    class Meta:
        model = AlbumSong
        fields = ['id', 'album', 'song', 'song_name', 'track_number', 'album_info', 'artist_name']


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