"""
AI Helper models for Smart College Helper Portal
Stores AI queries and responses
"""
from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class AIQuery(models.Model):
    """
    Stores all queries asked to AI Assistant
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='ai_queries')
    query = models.TextField()
    response = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['-created_at']
        verbose_name_plural = "AI Queries"
    
    def __str__(self):
        return f"{self.user.username} - {self.query[:50]}..."
