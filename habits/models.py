from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    pass

    def __str__(self):
        return self.username


class BaseModel(models.Model):
    created_at = models.DateTimeField(db_index=True, auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Habit(BaseModel):
    steps_taken = models.IntegerField()
    lines_written = models.IntegerField()
    new_people = models.IntegerField()
    pages_read = models.IntegerField()
    hours_slept = models.DecimalField(max_digits=3, decimal_places=1)
