from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework import generics
from rest_framework.viewsets import ViewSet
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.decorators import api_view,authentication_classes,permission_classes
from rest_framework.views import APIView
from rest_framework import status
from . import models
from django.shortcuts import render
from . import serializers
import pandas as pd
import re

class UserListView(generics.ListAPIView):
    queryset = models.CustomUser.objects.all()
    serializer_class = serializers.UserSerializer


class FileView(APIView):
  parser_classes = (MultiPartParser, FormParser)
  def post(self, request, *args, **kwargs):
    file_serializer = serializers.UploadSerializer(data=request.data)
    df=pd.DataFrame(request.FILES['file'])
    r,c=df.shape
    

    for i in range(1,r):
      n,s=df[0][i].split()
      n,s=int(n),s.decode("utf-8")
      # print(re.findall(r'[+]91\d{10}',str(n)),re.findall(r'\d{10}',str(n)))
      if re.findall('[+]91\d{10}',str(n)) or re.search('\d{10}',str(n)):
        b=models.FileDetailsSerializer(name=s,number=n)

        b.save()
    if file_serializer.is_valid():
      file_serializer.save()
      return Response(file_serializer.data, status=status.HTTP_201_CREATED)
    else:
      return Response(file_serializer.errors, status=status.HTTP_400_BAD_REQUEST)