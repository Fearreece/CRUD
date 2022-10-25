from email.policy import default
from pyexpat import model
from django.db import models

# Create your models here.
class Artiste(models.Model):
    firstname = models.CharField(max_length=30)
    lastname = models.CharField(max_length=30)
    age = models.CharField(max_length=30)

class Song(models.Model):
    title = models.CharField(max_length=30)
    date_released = models.DateField()
    likes = models.CharField(max_length=30)
    artiste_id = models.CharField(max_length=30)
    song = models.ForeignKey(Artiste, null=True, on_delete=models.SET_NULL)

class Lyric(models.Model):
    content = models.CharField(max_length=30)
    song_id = models.CharField(max_length=30)
    lyric = models.ForeignKey(Song, null=True,on_delete=models.SET_NULL)