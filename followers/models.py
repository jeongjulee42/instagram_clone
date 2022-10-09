from django.db import models
from core import models as core_models


class Follower(core_models.TimeStampedModel):
    
    """Follow models definition"""
    
    user = models.ForeignKey("users.User", related_name="follow", on_delete=models.CASCADE)
    follower_user = models.ManyToManyField("users.User", related_name="follow", blank=True, null=True)
