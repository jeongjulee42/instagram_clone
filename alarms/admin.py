from django.contrib import admin
from . import models


@admin.register(models.Alarm)
class AlarmAdmin(admin.ModelAdmin):
    pass