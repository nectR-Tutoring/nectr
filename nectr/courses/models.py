from django.db import models


class Courses(models.Model):
    subject = models.TextField()
    course_name = models.CharField(max_length=10)

    def __str__(self):
        return self.course_name
