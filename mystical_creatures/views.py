from django.shortcuts import render
from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView,
) 
from .models import Creatures as CreaturesModel
from .serializers import CreaturesSerializer

#  Create your views here.
class CreaturesList(ListCreateAPIView):
  queryset = CreaturesModel.objects.all()
  serializer_class = CreaturesSerializer

class CreaturesDetail(RetrieveUpdateDestroyAPIView):
  queryset = CreaturesModel.objects.all()
  serializer_class = CreaturesSerializer



