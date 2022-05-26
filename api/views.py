from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from habit.models import Habit
from .serializers import HabitSerializer
from rest_framework import generics

class HabitListView(APIView):
#   return JSON listof habit
    def get(self, request, format=None):
     
        habits     = Habit.objects.filter(user=request.user) 
        serializer = HabitSerializer(habits, many=True)
        return Response(serializer.data)


class HabitDetailView(generics.RetrieveDestroyAPIView):
    queryset          = Habit.objects.all()
    serializer_class  = HabitSerializer 


