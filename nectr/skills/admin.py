from django.contrib import admin

# Register your models here.
from nectr.skills.models import Skills


@admin.register(Skills)
class CourseAdmin(admin.ModelAdmin):
    pass
