from django.contrib import admin
from . import models


@admin.register(models.Conversation)
class ConversationAdmin(admin.ModelAdmin):
    
    """Conversation Admin pannel"""
    pass


@admin.register(models.Message)
class MessageAdmin(admin.ModelAdmin):
    pass