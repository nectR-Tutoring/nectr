from django.db import models

from nectr.courses.models import Courses
from nectr.student.models import Student
from nectr.users.models import User


class Tutor(models.Model):
    base_user = models.ForeignKey(User, on_delete=models.CASCADE)
    votes = models.IntegerField(default=0)
    courses = models.ManyToManyField(Courses)

