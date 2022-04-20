from django.db import models
from django.contrib.auth.models import User
from django.db.models import UniqueConstraint
from datetime import date

# Create your models here.
class Habit(models.Model):

    created_at = models.DateTimeField(auto_now_add=True)

    updated_at = models.DateTimeField(auto_now=True)

    owner = models.ForeignKey(User, related_name='habits', on_delete=models.CASCADE)

    title = models.CharField(max_length=64) # name of your new habit

    action = models.CharField(max_length=64) # what action are you performing for this habit

    units = models.CharField(max_length=64, default='times') # what units/how many times you want to do your habit

    goal = models.PositiveIntegerField(default=0) # how much to accomplish daily
  

    def __str__(self) -> str:

        return self.title

class HabitLog(models.Model):
    
    created_at = models.DateTimeField(auto_now_add=True)

    updated_at = models.DateTimeField(auto_now=True)

    date = models.DateField(default=date.today)

    achievement = models.PositiveIntegerField(default=0) # how much/many times you did your habit

    habit = models.ForeignKey(Habit, on_delete=models.CASCADE, related_name='logs')

    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='logs')

    def __str__(self) -> str:

        return self.date
        
        # f"{self.owner.username}'s {self.habit.title} on {self.date}"

    class Meta:

        ordering = ['-date']

        constraints = [models.UniqueConstraint(fields=['date', 'habit', 'owner'], name='unique_log')]