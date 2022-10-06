from django.db import models


class TimeStampedModel(models.Model):
    
    """Time Model Definition"""
    
    created = models.DateTimeField(auto_now_add=True, null=True)
    update = models.DateTimeField(auto_now=True, null=True)
    
    class Meta:
        abstract = True