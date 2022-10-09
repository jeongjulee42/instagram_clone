from email.policy import default
from django.db import models
from core import models as core_models


class Like(core_models.TimeStampedModel):
    
    """Like Model definition"""
    
    count = models.IntegerField(default=0)
    user = models.ForeignKey("users.User", related_name="likes", on_delete=models.CASCADE)
    post = models.ForeignKey("posts.Post", related_name="likes", on_delete=models.CASCADE)