from django.db import models


class Search(models.Model):
    search_text = models.TextField()
