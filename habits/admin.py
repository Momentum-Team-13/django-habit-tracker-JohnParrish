from django.contrib import admin
from .models import Habit, User, Habit_Tracker


admin.site.register(Habit)
admin.site.register(User)
admin.site.register(Habit_Tracker)
