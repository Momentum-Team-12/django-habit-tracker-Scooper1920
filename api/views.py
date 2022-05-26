from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from habit.models import Habit, CustomUser, DateRecord
from .serializers import HabitSerializer, CustomUserSerializer, DateRecordSerializer
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

class CustomUserListView(generics.ListAPIView):
    queryset         = CustomUser.objects.all()
    serializer_class = CustomUserSerializer

class CustomUserDetailView(generics.RetrieveAPIView):
    queryset         = CustomUser.objects.all()
    serializer_class = CustomUserSerializer

class DateRecordView(generics.ListCreateAPIView):
    queryset          = DateRecord.objects.all()
    serializer_class  = DateRecordSerializer

class DateRecordDetailView(generics.RetrieveDestroyAPIView):
    queryset          = DateRecord.objects.all()
    serializer_class  = DateRecordSerializer