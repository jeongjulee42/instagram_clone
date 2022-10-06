from django.db import models
from django_countries.fields import CountryField
from core import models as core_models


class Post(core_models.TimeStampedModel):
    
    """Post Model Definition"""
    
    host = models.ForeignKey("users.User", related_name="posts", on_delete=models.CASCADE, null=True)
    description = models.TextField(null=True)
    country = CountryField(null=True, blank=True)
    city = models.CharField(max_length=80, null=True, blank=True)
    is_private = models.BooleanField(default=False)
    
    
class Photo(core_models.TimeStampedModel):
    
    """Photo Model Definition"""
    
    file = models.ImageField(null=True)
    Post = models.ForeignKey("Post", related_name="photos", on_delete=models.CASCADE)