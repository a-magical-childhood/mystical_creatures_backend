from django.shortcuts import render
from rest_framework import generics
 
from .models import Creatures
from .serializers import CreaturesSerializer

#  Create your views here.
class Creatures(generics.ListCreateAPIView):
  queryset = Creatures.objects.all()
  serializer_class = CreaturesSerializer

class Sightings(generics.RetrieveUpdateDestroyAPIView):
  queryset = Creatures.objects.all()
  serializer_class = CreaturesSerializer



