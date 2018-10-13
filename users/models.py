from django.db import models
from django.contrib.auth.models import User
from PIL import Image

class Profile(models.Model):
    user = models.OneToOneField(User,on_delete= models.CASCADE)
    image = models.ImageField(default = 'default.jpg',upload_to='_profile_pics')


    def __str__(self):
        return f'{self.user.username} Profile'


#class Song(models.Model):
#    title = models.CharField(max_length=100)
#    songfile = models.FileField(upload_to='_audio_files')
#    duration = models.FloatField()
#    isPlaying = False
#    user = models.OneToOneField(User,on_delete= models.CASCADE)


#    def __str__(self):
#        return self.title
class Video(models.Model):
    name = models.CharField(max_length=500)
    videofile= models.FileField(upload_to='videos/',null = True,verbose_name="")
    views_count = models.IntegerField(default=170)
    def __str__(self):
            return self.name+":"+str(self.videofile)

class Audio(models.Model):
    name = models.CharField(max_length=500)
    audiofile= models.FileField(upload_to='audios/',null = True,verbose_name="")
    #views_count = models.IntegerField(default=170)
    def __str__(self):
            return self.name+":"+str(self.audiofile)
