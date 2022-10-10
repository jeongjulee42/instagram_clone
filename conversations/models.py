from django.db import models
from core import models as core_models


class Conversation(core_models.TimeStampedModel):
    
    """Conversation model definition"""
    
    participants = models.ManyToManyField("users.User", related_name="conversation", blank=True)
    
    
class Message(core_models.TimeStampedModel):
    
    """Message models definition"""
    
    message = models.TextField()
    user = models.ForeignKey("users.User", related_name="messages", on_delete=models.CASCADE)
    conversation = models.ForeignKey("conversations.Conversation", related_name="messages", on_delete=models.CASCADE)

