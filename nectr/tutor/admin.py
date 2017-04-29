from django.contrib import admin

# Register your models here.
from nectr.tutor.models import Tutor


@admin.register(Tutor)
class AuthorAdmin(admin.ModelAdmin):
    pass
