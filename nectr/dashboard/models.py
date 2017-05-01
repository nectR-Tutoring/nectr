from django.db import models

# Create your models here.
from nectr.users.models import User


class Dashboard(models.Model):
    user = models.ForeignKey(User)
