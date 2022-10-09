from django.db import models
from core import models as core_models


class Message(core_models.TimeStampedModel):
    
    """Message models definition"""
    
    message = models.TextField()
    user = models.ForeignKey("users.User", related_name="message", on_delete=models.CASCADE)
    conversation = models.ForeignKey("conversations.Conversation", related_name="message", on_delete=models.CASCADE)

