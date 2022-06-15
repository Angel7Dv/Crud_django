from django.db import models

# Create your models here.


class List(models.Model):
    name = models.CharField(max_length=200)


class Task(models.Model):

    name = models.CharField(max_length=200)
    list = models.ForeignKey(List, related_name='todos', on_delete=models.CASCADE, null=True, blank=True)
    checked = models.BooleanField(default=False)
    description = models.TextField()
