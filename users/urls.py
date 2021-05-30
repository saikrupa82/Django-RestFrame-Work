from django.urls import include, path
from rest_framework import routers
from .views import *

urlpatterns = [
  
    path('', UserListView.as_view()),
    path('upload/', FileView.as_view(), name='file-upload'),
  ]