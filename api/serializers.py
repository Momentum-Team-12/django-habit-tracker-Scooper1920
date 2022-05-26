from rest_framework import serializers
from habit.models import Habit, CustomUser, DateRecord

class HabitSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    
    class Meta:
        model = Habit
        fields = ('name', 'goal', 'user', 'unit', 'planstart', 'journal', 'owner')


class CustomUserSerializer(serializers.ModelSerializer):
    habits = serializers.PrimaryKeyRelatedField(many=True, queryset=Habit.objects.all())
    
    class Meta:
        model   = CustomUser
        fields  = ('id','username','habits')


class DateRecordSerializer(serializers.ModelSerializer):

    class Meta:
        model  = DateRecord
        fields = ('habit', 'actual', 'date')
    