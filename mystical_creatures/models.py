from django.db import models

# Create your models here.

class Creatures(models.Model):
  id = models.IntegerField
  creature_name = models.CharField
  latitude = models.CharField
  longitude = models.CharField
  description = models.CharField(default = "option")
  explorer = models.CharField(default = "option")

  def __str__(self):
    return self.creature_name + self.description