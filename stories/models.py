from django.db import models
from core import models as core_models


class Story(core_models.TimeStampedModel):
    
    """Story models definition"""
    
    host = models.ForeignKey("users.User", related_name="stories", on_delete=models.CASCADE, null=True)
    story_text = models.TextField(null=True, blank=True)
    is_private = models.BooleanField(default=False)
    

class StotyPhoto(core_models.TimeStampedModel):
    
    """Photo Model in Stories Definition"""
    
    file = models.ImageField(null=True)
    story = models.ForeignKey("Story", related_name="story_photos", on_delete=models.CASCADE)
    
    