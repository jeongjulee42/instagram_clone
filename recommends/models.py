from django.db import models


class Recommend(models.Model):
    
    """Recommend models definition"""
    
    host = models.ForeignKey("users.User", related_name="recommends", on_delete=models.CASCADE)
    recommendList = models.ManyToManyField("users.User", related_name="recommendList", blank=True)