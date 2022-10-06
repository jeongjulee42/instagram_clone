from django.db import models


class TimeStampedModel(models.Model):
    
    """Time Model Definition"""
    
    created = models.DateTimeField()
    update = models.DateTimeField()
    
    class Meta:
        abstract = True