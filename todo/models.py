from django.db import models
from django.contrib.auth.models import User
from slugger import AutoSlugField

# Create your models here.
class Tag(models.Model):

    tag = models.CharField(max_length=200, unique=True)

    slug = AutoSlugField(populate_from='tag')

    def __str__(self) -> str:
        
        return self.tag

class Todo(models.Model):

    owner = models.ForeignKey(User, related_name='todo_list', on_delete=models.CASCADE)

    title = models.CharField(max_length=225, unique=True)

    slug = AutoSlugField(populate_from='title')

    details = models.CharField(max_length=225)

    completed = models.BooleanField(default=False)

    tags = models.ForeignKey(Tag, blank=True, related_name='todo_list', on_delete=models.CASCADE)

    def __str__(self) -> str:
        
        return self.title