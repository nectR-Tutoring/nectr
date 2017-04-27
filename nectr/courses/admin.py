from django.contrib import admin

# Register your models here.
from nectr.courses.models import Courses


@admin.register(Courses)
class AuthorAdmin(admin.ModelAdmin):
    pass
