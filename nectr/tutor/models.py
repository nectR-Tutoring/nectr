from django.db import models
from django.urls import reverse

from nectr.courses.models import Courses
from nectr.users.models import User


class Tutor(models.Model):
    user = models.ForeignKey(User, default=1, null=True)
    votes = models.IntegerField(default=0)
    courses = models.ManyToManyField(Courses)
    skills = models.ManyToManyField(Skills)
    bio = models.TextField(default='No Bio Provided')

    def __str__(self):
        return self.user.username

    def get_absolute_url(self):
        return reverse('tutors:detail', kwargs={'username': self.user.username})
