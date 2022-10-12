from email.policy import default
from django.db import models
from core import models as core_models


class Alarm(core_models.TimeStampedModel):
    
    """Alarm models definition"""
    
    ALARM_FOLLOW = "follow"
    ALARM_POST = "post"
    ALARM_STORY = "story"
    ALARM_MESSAGE = "message"
    ALARM_CHOICES = (
        (ALARM_FOLLOW, "Follow"),
        (ALARM_POST, "Post"),
        (ALARM_STORY, "Story"),
        (ALARM_MESSAGE, "Message"),
    )
    
    host = models.ForeignKey("users.User", related_name="alarm", on_delete=models.CASCADE)
    post = models.ForeignKey("posts.Post", related_name="alarm", on_delete=models.CASCADE, null=True)
    story = models.ForeignKey("stories.Story", related_name="alarm", on_delete=models.CASCADE, null=True)
    conversation = models.ForeignKey("conversations.Conversation", related_name="alarm", on_delete=models.CASCADE, null=True)
    alarmType = models.CharField(max_length=7, choices=ALARM_CHOICES, default=ALARM_POST)
    is_checked = models.BooleanField(default=False)
