from django.contrib.auth.models import User
from django.db import models
from django.core.validators import FileExtensionValidator
# Create your models here.
class Lecture(models.Model):
    title = models.CharField(max_length=100)
    video = models.FileField(upload_to='videos_uploaded', null=True, validators=[FileExtensionValidator(allowed_extensions=['MOV','avi','mp4','webm','mkv'])])

    def __str__(self):
        return self.title

class Short(models.Model):
    lecture = models.ForeignKey(Lecture, on_delete=models.CASCADE)
    segment = models.CharField(max_length=1000, null=True, blank=True)
    keyword1 = models.CharField(max_length=20, null=True, blank=True)
    keyword2 = models.CharField(max_length=20, null=True, blank=True)
    keyword3 = models.CharField(max_length=20, null=True, blank=True)
    reason = models.CharField(max_length=100, null=True, blank=True)
    short_video = models.FileField(upload_to='short_videos', null=True, validators=[FileExtensionValidator(allowed_extensions=['MOV','avi','mp4','webm','mkv'])])