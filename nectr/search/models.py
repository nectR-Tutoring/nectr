from django.db import models

# Create your models here.
class Search(models.Model):
    search_text = models.TextField(default='No Search Given')
