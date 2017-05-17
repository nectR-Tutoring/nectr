from django.db import models


class Schedule(models.Model):
    day_of_week = models.TextField(default='')

    def __str__(self):
        return self.day_of_week
