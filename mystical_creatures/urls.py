from django.urls import path
from .views import CreaturesList, CreaturesDetail
 
urlpatterns = [
  path('', CreaturesList.as_view(), name="creatures"),
  path('sightings/<int:pk>/', CreaturesDetail.as_view(), name="creatures_details"),
]
