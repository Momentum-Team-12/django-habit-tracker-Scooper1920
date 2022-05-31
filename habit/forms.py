from django import forms
from .models import Habit
from .models import DateRecord



class HabitForm(forms.ModelForm):
    class Meta:
        model = Habit
        fields = (
            'name',
            'goal',
            'unit',
            'planstart',
            'journal',
            
        )


class DateRecordForm(forms.ModelForm):
        class Meta:
            model   = DateRecord
            fields  = (

                'actual',
                'date',
            )