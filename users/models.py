from django.contrib.auth.models import AbstractUser
from rest_framework.serializers import Serializer, FileField
from django.db import models

class CustomUser(AbstractUser):
    name = models.CharField(blank=True, max_length=255)

    def __str__(self):
        return self.email


class UploadSerializer(models.Model):
  file = models.FileField(blank=False, null=False)
  remark = models.CharField(max_length=20)
  timestamp = models.DateTimeField(auto_now_add=True)

class FileDetailsSerializer(models.Model):
  auto_increment_id = models.AutoField(primary_key=True)
  name = models.CharField(max_length=100,blank=False, null=False)
  number = models.IntegerField()
    