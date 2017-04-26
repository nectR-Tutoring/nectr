from django.db import models

from nectr.users.models import User


class Tutor(models.Model):
    user = models.ForeignKey(User)
