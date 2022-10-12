from django.contrib import admin
from . import models


@admin.register(models.Post)
class PostAdmin(admin.ModelAdmin):
    pass


@admin.register(models.PostPhoto)
class PhotoAdmin(admin.ModelAdmin):
    pass