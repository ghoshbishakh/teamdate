from django.db import models

# Create your models here.


class Event(models.Model):
    date_time = models.DateTimeField()
    name = models.CharField(max_length=255)
    description = models.TextField()
