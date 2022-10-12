from django.db import models
from core import models as core_models


class Follow(core_models.TimeStampedModel):
    
    """Follow models definition"""
    
    host = models.ForeignKey("users.User", related_name="follows", on_delete=models.CASCADE)
    follow = models.ManyToManyField("users.User", related_name="followList", blank=True)
    
    
class Follower(core_models.TimeStampedModel):
    
    """Follow models definition"""
    
    host = models.ForeignKey("users.User", related_name="followers", on_delete=models.CASCADE)
    follower = models.ManyToManyField("users.User", related_name="followerList", blank=True)
