from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Todo(models.Model):

    CHOICES_TAGS = (
        ('health', 'Health'),
        ('work', 'Work'),
        ('home', 'Home'),
        ('social', 'Social'),
        ('outdoor', 'Outdoor'),
        ('other', 'Other'),
    )

    owner = models.ForeignKey(User, related_name='todo_list', on_delete=models.CASCADE)

    title = models.CharField(max_length=225, unique=True)

    details = models.CharField(max_length=225)

    completed = models.BooleanField(default=False)

    tags = models.CharField(max_length=50, choices=CHOICES_TAGS)

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:

        ordering = ['-created_at']

    def __str__(self) -> str:
        
        return self.title