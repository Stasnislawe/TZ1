from django.core.validators import MinValueValidator
from django.db import models


class Artist(models.Model):
    """Модель исполнителя"""
    name = models.CharField(max_length=255, verbose_name='Название')

    class Meta:
        verbose_name = 'Исполнитель'
        verbose_name_plural = 'Исполнители'

    def __str__(self):
        return self.name


class Album(models.Model):
    """Модель альбома"""
    release_year = models.PositiveIntegerField(verbose_name='Год выпуска', validators=[MinValueValidator(1860)])
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE, related_name='albums', verbose_name='Исполнитель')

    class Meta:
        verbose_name = 'Альбом'
        verbose_name_plural = 'Альбомы'

    def __str__(self):
        return f"({self.release_year})"


class Song(models.Model):
    """Модель песни"""
    name = models.CharField(max_length=255, verbose_name='Название песни')
    albums = models.ManyToManyField(
        Album,
        through='AlbumSong',
        through_fields=('song', 'album'),
        verbose_name='Альбомы'
    )

    class Meta:
        verbose_name = 'Песня'
        verbose_name_plural = 'Песни'

    def __str__(self):
        return self.name


class AlbumSong(models.Model):
    """Промежуточная модель для связи альбома и песни с порядковым номером"""
    album = models.ForeignKey(Album, on_delete=models.CASCADE, related_name='album_songs')
    song = models.ForeignKey(Song, on_delete=models.CASCADE, related_name='song_albums')
    track_number = models.PositiveIntegerField(
        verbose_name='Порядковый номер',
        validators=[MinValueValidator(1)]
    )

    class Meta:
        unique_together = [
            ['album', 'track_number'],
            ['album', 'song']
        ]