from django.db import models

from nectr.courses.models import Courses
from nectr.student.models import Student
from nectr.users.models import User


class Tutor(User):
    # Possibly define my own link back to parent if necessary
    # user_ptr = models.OneToOneField(
    #     User, on_delete=models.CASCADE,
    #     parent_link=True,
    # )
    votes = models.IntegerField(default=0)
    courses = models.ManyToManyField(Courses)

    def __str__(self):
        return self.username
