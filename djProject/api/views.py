from django.shortcuts import render
from rest_framework import generics
from .serializers import RoomSerializer
from .models import Room

# Create your views here.
class RoomView(generics.ListAPIView):
    queryset = Room.objects.all() # returns all Rooms in database
    serializer_class = RoomSerializer # translates all Rooms to something we can use