from django.shortcuts import render
from .models import Habit


def see_habits(request):
    habits = Habit.objects.all()
    return render(request, 'habits/see_habits.html', {'habits': habits})


def home(request):
    return render(request, 'home.html')
