from rest_framework import serializers
from habit.models import Habit

class HabitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Habit
        fields = ('name', 'goal', 'user', 'unit', 'planstart', 'journal')