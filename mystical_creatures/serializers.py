from rest_framework import serializers
from .models import Creatures
class CreaturesSerializer(serializers.ModelSerializer):
  class Meta:
    fields = (any fields in the model)
    model = Creatures