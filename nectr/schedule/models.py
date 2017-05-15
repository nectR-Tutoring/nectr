from django.db import models


class Schedule(models.Model):
    monday = models.BooleanField(default=0)
    tuesday = models.BooleanField(default=0)
    wednesday = models.BooleanField(default=0)
    thursday = models.BooleanField(default=0)
    friday = models.BooleanField(default=0)
    saturday = models.BooleanField(default=0)
    sunday = models.BooleanField(default=0)
