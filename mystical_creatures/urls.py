from django.urls import path
from .views import Creatures
 
urlpatterns = [
  path('', creatures.as_view(), name="creatures"),
  path('<int:pk>/', sightings.as_view(), name="sightings"),
]
