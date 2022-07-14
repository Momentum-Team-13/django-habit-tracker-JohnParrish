from django import forms
from .models import User, Habit, Habit_Tracker


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = [
            'first_name',
            'last_name',
        ]


class HabitForm(forms.ModelForm):
    class Meta:
        model = Habit
        fields = [
            'title',
            'description',
            'goal',
            'unit',
            'creator',
        ]


class Habit_TrackerForm(forms.ModelForm):
    class Meta:
        model = Habit_Tracker
        fields = [
            'habit',
            'date',
            'tracking_unit',
        ]
