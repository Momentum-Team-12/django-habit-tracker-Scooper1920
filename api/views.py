from rest_framework import generics, permissions
from rest_framework.decorators import api_view
from rest_framework.response import Response 
from rest_framework.reverse import reverse

from habit.models import Habit, CustomUser, DateRecord
from .serializers import HabitSerializer, CustomUserSerializer, DateRecordSerializer
from .permission import IsOwnerOrReadOnly 



@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'users': reverse('user-list', request=request, format=format),
        'habits': reverse('habit-list', request=request, format=format),
        'daterecords':reverse('date-record-list', request=request, format=format),
    })


class HabitListView(generics.ListCreateAPIView):
    queryset            = Habit.objects.all()
    serializer_class    = HabitSerializer
    permission_classes  = (permissions.IsAuthenticatedOrReadOnly,)

    def perform_create(self,serializer):
        serializer.save(owner=self.request.user)
        


class HabitDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset          = Habit.objects.all()
    serializer_class  = HabitSerializer 
    permission_classes  = (permissions.IsAuthenticatedOrReadOnly,IsOwnerOrReadOnly)

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
    permission_classes  = (permissions.IsAuthenticatedOrReadOnly,IsOwnerOrReadOnly)