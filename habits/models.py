from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.constraints import UniqueConstraint
import datetime


class User(AbstractUser):
    first_name = models.CharField(max_length=255, primary_key=True)
    last_name = models.CharField(max_length=255)

    def __str__(self):
        return self.username


class Habit(models.Model):
    title = models.CharField(max_length=255, primary_key=True)
    description = models.CharField(max_length=255)
    goal = models.IntegerField(default=0)
    unit = models.CharField(max_length=255)
    creator = models.ForeignKey(User, on_delete=models.CASCADE, related_name="habits")


class Habit_Tracker(models.Model):
    habit = models.ForeignKey(Habit, primary_key=True, on_delete=models.CASCADE, related_name="habit_trackers")
    date = models.DateField(default=datetime.date.today)
    tracking_unit = models.IntegerField(default=0)

    class meta:
        constriants = [
            UniqueConstraint(fields=['habit', 'date'], name='unique_habit_date')
            ]
