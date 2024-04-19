from django.contrib.auth.models import User
from django.db import models
from django.core.validators import FileExtensionValidator
# Create your models here.
class Lecture(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    lecture_name = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    video = models.FileField(upload_to='videos_uploaded', null=True, validators=[FileExtensionValidator(allowed_extensions=['MOV','avi','mp4','webm','mkv'])])

class Short(models.Model):
    lecture = models.ForeignKey(Lecture, on_delete=models.CASCADE)
    semi_title = models.CharField(max_length=100)
    short_video = models.FileField(upload_to='short_videos', null=True, validators=[FileExtensionValidator(allowed_extensions=['MOV','avi','mp4','webm','mkv'])])