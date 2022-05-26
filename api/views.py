from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics, permissions

from habit.models import Habit, CustomUser, DateRecord
from .serializers import HabitSerializer, CustomUserSerializer, DateRecordSerializer


class HabitListView(generics.ListCreateAPIView):
    queryset            = Habit.objects.all()
    serializer_class    = HabitSerializer
    permission_classes  = (permissions.IsAuthenticatedOrReadOnly,)

    def perform_create(self,serializer):
        serializer.save(owner=self.request.user)
        


class HabitDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset          = Habit.objects.all()
    serializer_class  = HabitSerializer 
    permission_classes  = (permissions.IsAuthenticatedOrReadOnly,)

class CustomUserListView(generics.ListAPIView):
    queryset         = CustomUser.objects.all()
    serializer_class = CustomUserSerializer

class CustomUserDetailView(generics.RetrieveAPIView):
    queryset            = CustomUser.objects.all()
    serializer_class    = CustomUserSerializer
    permission_classes  = (permissions.IsAuthenticatedOrReadOnly,)

class DateRecordView(generics.ListCreateAPIView):
    queryset          = DateRecord.objects.all()
    serializer_class  = DateRecordSerializer

class DateRecordDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset            = DateRecord.objects.all()
    serializer_class    = DateRecordSerializer
    permission_classes  = (permissions.IsAuthenticatedOrReadOnly,)