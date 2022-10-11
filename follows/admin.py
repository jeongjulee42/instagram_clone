from django.contrib import admin
from . import models


@admin.register(models.Follow)
class FollowAdmin(admin.ModelAdmin):
    
    """Follow admin pannel"""
    
    pass


@admin.register(models.Follower)
class FollowerAdmin(admin.ModelAdmin):
    
    """Follower admin pannel"""
    
    pass