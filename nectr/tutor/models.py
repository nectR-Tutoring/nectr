from django.db import models

from nectr.student.models import Student
from nectr.users.models import User


class Tutor(models.Model):
    user = models.ForeignKey(User)
    student = models.ForeignKey(Student)
