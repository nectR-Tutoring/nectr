from django.contrib import admin

# Register your models here.
from nectr.courses.models import Courses


@admin.register(Courses)
class CourseAdmin(admin.ModelAdmin):
    pass
