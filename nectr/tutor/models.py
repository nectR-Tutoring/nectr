from django.db import models

from nectr.courses.models import Courses
from nectr.users.models import User


class Tutor(models.Model):
    # Possibly define my own link back to parent if necessary
    # user_ptr = models.OneToOneField(
    #     User, on_delete=models.CASCADE,
    #     parent_link=True,
    # )
    user = models.ForeignKey(User, default=1, null=True)
    votes = models.IntegerField(default=0)
    courses = models.ManyToManyField(Courses)

    def __str__(self):
        return self.user.username
