from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.constraints import UniqueConstraint
import datetime


class User(AbstractUser):
    # first_name = models.CharField(max_length=255, null=True, blank=True)
    # last_name = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.username


class Habit(models.Model):
    title = models.CharField(max_length=255, null=True, blank=True)
    description = models.CharField(max_length=255, null=True, blank=True)
    goal = models.IntegerField(default=0)
    unit = models.CharField(max_length=255, null=True, blank=True)
    creator = models.ForeignKey(User, on_delete=models.SET_NULL, related_name='creator',null=True, blank=True)


class Habit_Tracker(models.Model):
    habit = models.ForeignKey(Habit, on_delete=models.SET_NULL, related_name="habit_trackers", null=True, blank=True)
    date = models.DateField(default=datetime.date.today)
    tracking_unit = models.IntegerField(default=0)

    class meta:
        constriants = [
            UniqueConstraint(fields=['habit', 'date'], name='unique_habit_date')
            ]
