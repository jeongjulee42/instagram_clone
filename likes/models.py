from email.policy import default
from django.db import models
from core import models as core_models


class Like(core_models.TimeStampedModel):
    
    """Like Model definition"""
    
    post = models.ForeignKey("posts.Post", related_name="likes", on_delete=models.CASCADE)
    userList = models.ManyToManyField("users.User", related_name="userList", blank=True)