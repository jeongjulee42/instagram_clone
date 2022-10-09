from django.db import models
from core import models as core_models


class Conversation(core_models.TimeStampedModel):
    
    """Conversation model definition"""
    
    participants = models.ManyToManyField("users.User", related_name="conversation", blank=True)