from django.db import models


class Song(models.Model):
    title = models.CharField(max_length=100)
    file = models.FileField(upload_to="songs/")
    class Meta:
        app_label = "music_player"