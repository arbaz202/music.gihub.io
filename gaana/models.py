import datetime
from django.contrib.auth.models import User
from django.db import models
from django.conf.urls import url
from django.core.validators import FileExtensionValidator
# Create your models here.
class Album(models.Model):
    title=models.CharField(max_length=100,null=False,help_text='album title')
    artist=models.CharField(max_length=50,help_text='album artist')
    genre=models.CharField(max_length=20,help_text='album genre')
    year=models.DateField(help_text='release date')
    image=models.FileField(validators=[FileExtensionValidator(['jpg','png'])])
    
    def __str__(self):
        return 'title:{},artist:{}'.format(self.title,self.artist)
class Profile(models.Model):


    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    photo = models.FileField(default='settings.MEDIA_ROOT/def.jpg')
    DOB = models.DateField(default=datetime.datetime.today())
    city = models.CharField(max_length=100)

    def __str__(self):
        return self.user.username


class Song(models.Model):
    al_id=models.ForeignKey(Album,on_delete=models.CASCADE)
    title=models.CharField(max_length=100,null=False,help_text='Song title')
    artist=models.CharField(max_length=50,help_text='Song artist')
    genre=models.CharField(max_length=20,help_text='Song genre')
    sfile=models.FileField(validators=[FileExtensionValidator(['mp3','aac'])])
    image=models.FileField(validators=[FileExtensionValidator(['jpg','png'])])
    isPlaying = False

    def __str__(self):
        return 'title:{},artist:{}'.format(self.title,self.artist)


class ShipPhoto(models.Model):
    user_name      = models.ForeignKey(User, on_delete=models.CASCADE)
    photo          = models.ImageField()
    voice_record = models.FileField(default=False)

    carplates      = models.CharField(max_length=20)