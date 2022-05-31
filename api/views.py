from psycopg2 import Date
from rest_framework import generics, permissions
from rest_framework.decorators import api_view
from rest_framework.response import Response 
from rest_framework.reverse import reverse
from rest_framework.views import APIView

from habit.models import Habit, CustomUser, DateRecord
from .serializers import HabitSerializer, CustomUserSerializer, DateRecordSerializer
# from .permission import IsOwnerOrReadOnly 



@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'users': reverse('user-list', request=request, format=format),
        'habits': reverse('habit-list-api', request=request, format=format),
        'daterecords':reverse('date-record-list', request=request, format=format),
    })


class HabitListView(APIView):
    
    def get(self,request, format=None):
        habits = Habit.objects.filter(user=request.user)
        serializer = HabitSerializer(habits, many=True)
        return Response(serializer.data)
    

class HabitCreateView(generics.CreateAPIView):
    queryset            = Habit.objects.all()
    serializer_class    = HabitSerializer
    permission_classes  = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self,serializer):
        serializer.save(user=self.request.user) 


class HabitDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset          = Habit.objects.filter()
    serializer_class  = HabitSerializer 
    permission_classes  = [permissions.IsAuthenticatedOrReadOnly]
    

    def perform_destroy(self, instance):
       
        if instance.user == self.request.user:
            instance.delete()

    def perform_create(self,serializer):
            serializer.save(user=self.request.user)
    
    def perform_update(self, serializer):
            serializer.save(user=self.request.user)


class CustomUserListView(generics.ListAPIView):
    queryset         = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
    permission_classes  = [permissions.IsAuthenticatedOrReadOnly]

class CustomUserDetailView(generics.RetrieveAPIView):
    queryset            = CustomUser.objects.all()
    serializer_class    = CustomUserSerializer
    permission_classes  = [permissions.IsAuthenticatedOrReadOnly]

class DateRecordView(generics.ListCreateAPIView):
    queryset          = DateRecord.objects.all()
    serializer_class  = DateRecordSerializer
    permission_classes  = [permissions.IsAuthenticatedOrReadOnly]

class DateRecordCreateView(generics.CreateAPIView):
    queryset            = DateRecord.objects.all()
    serializer_class    = DateRecordSerializer
    permission_classes  = [permissions.IsAuthenticatedOrReadOnly]
    
    def perform_create(self,serializer):
        serializer.save(user=self.request.user)

class DateRecordDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset            = DateRecord.objects.all()
    serializer_class    = DateRecordSerializer
    permission_classes  = [permissions.IsAuthenticatedOrReadOnly]

    def perform_destroy(self, instance):
        if instance.habit.user == self.request.user:
            instance.delete()

    def perform_create(self,serializer):
            serializer.save(user=self.request.user)
    
    def perform_update(self, serializer):
            serializer.save(user=self.request.user)

   