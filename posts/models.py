from django.db import models
from django_countries.fields import CountryField
from core import models as core_models


class Post(core_models.TimeStampedModel):
    
    host = models.ForeignKey("users.User", related_name="posts", on_delete=models.CASCADE)
    description = models.TextField(null=True)
    country = CountryField(null=True, blank=True)
    city = models.CharField(max_length=80, null=True, blank=True)
    is_private = models.BooleanField(dafault=False)