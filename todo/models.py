from django.db import models

# Create your models here.
class Tag(models.Model):

    tag = models.CharField(max_length=200, unique=True)

    slug = models.SlugField(max_length=200, unique=True)

    def __str__(self) -> str:
        
        return self.tag

class Todo(models.Model):

    title = models.CharField(max_length=225, unique=True)

    slug = models.SlugField(max_length=225, unique=True)

    details = models.CharField(max_length=225)

    completed = models.BooleanField(default=False)

    tags = models.ManyToManyField(Tag, blank=True)

    def __str__(self) -> str:
        
        return self.title