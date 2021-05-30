from rest_framework import serializers
from . import models

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.CustomUser
        fields = ('email', 'username', )

class UploadSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.UploadSerializer
        fields = ('file', 'remark', 'timestamp')
        
class FileDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.FileDetailsSerializer
        fields = ('name', 'number')
