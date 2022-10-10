from django.db import models
from core import models as core_models


class Story(core_models.TimeStampedModel):
    
    """Story models definition"""
    
    host = models.ForeignKey("users.User", related_name="stories", on_delete=models.CASCADE, null=True)
    story_text = models.TextField(null=True, blank=True)
    

