from django.db import models
from datetime import datetime

# Create your models here.
class Artiste(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    age = models.IntegerField()

class Song(models.Model):
    title = models.CharField(max_length=100)
    date_released = models.DateField(datetime.today)
    likes = models.IntegerField()
    artiste_id = models.CharField(max_length=100)

    artiste_id = models.ForeignKey(Artiste, on_delete=models.CASCADE)


class Lyric(models.Model):
    content = models.TextField(max_length=10000)
    song_id = models.IntegerField()

    song_id = models.ForeignKey(Song, on_delete=models.CASCADE)