from django.shortcuts import render, redirect
from .models import Habit
from django.contrib.auth.decorators import login_required


def home(request):
    if request.user.is_authenticated:
        return redirect('see_habits')
    return render(request, 'habits/home.html')


@login_required
def see_habits(request):
    habits = Habit.objects.all()
    return render(request, 'habits/see_habits.html', {'habits': habits})
