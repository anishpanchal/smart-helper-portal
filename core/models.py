"""
Core models for Smart College Helper Portal
Includes Notes, Study Plans, Notices, and Placement Roadmaps
"""
from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Subject(models.Model):
    """Subject/Course model"""
    name = models.CharField(max_length=200)
    code = models.CharField(max_length=20, unique=True)
    semester = models.IntegerField()
    
    def __str__(self):
        return f"{self.name} (Sem {self.semester})"


class Note(models.Model):
    """
    Notes/Resources uploaded by admin
    Students can view and download
    """
    title = models.CharField(max_length=200)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, related_name='notes')
    file = models.FileField(upload_to='notes/')
    description = models.TextField(blank=True, null=True)
    uploaded_by = models.ForeignKey(User, on_delete=models.CASCADE)
    uploaded_at = models.DateTimeField(auto_now_add=True)
    download_count = models.IntegerField(default=0)
    
    class Meta:
        ordering = ['-uploaded_at']
    
    def __str__(self):
        return self.title


class StudyPlan(models.Model):
    """
    AI-generated study plans for students
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='study_plans')
    course_name = models.CharField(max_length=200)
    exam_date = models.DateField()
    hours_per_day = models.IntegerField()
    plan_data = models.JSONField()  # Stores day-wise study plan
    created_at = models.DateTimeField(auto_now_add=True)
    is_completed = models.BooleanField(default=False)
    
    class Meta:
        ordering = ['-created_at']
    
    def __str__(self):
        return f"{self.user.username} - {self.course_name}"


class Notice(models.Model):
    """
    College notices uploaded by admin
    """
    title = models.CharField(max_length=200)
    content = models.TextField()
    file = models.FileField(upload_to='notices/', blank=True, null=True)
    posted_by = models.ForeignKey(User, on_delete=models.CASCADE)
    posted_at = models.DateTimeField(auto_now_add=True)
    is_important = models.BooleanField(default=False)
    
    class Meta:
        ordering = ['-posted_at']
    
    def __str__(self):
        return self.title


class PlacementRoadmap(models.Model):
    """
    Career path roadmaps (Data Analyst, AI/ML Engineer, Web Developer, etc.)
    """
    CAREER_CHOICES = [
        ('data_analyst', 'Data Analyst'),
        ('ai_ml_engineer', 'AI/ML Engineer'),
        ('web_developer', 'Web Developer'),
        ('software_engineer', 'Software Engineer'),
        ('cybersecurity', 'Cybersecurity Specialist'),
    ]
    
    career_path = models.CharField(max_length=50, choices=CAREER_CHOICES, unique=True)
    title = models.CharField(max_length=200)
    description = models.TextField()
    skills = models.JSONField()  # List of skills
    tools = models.JSONField()  # List of tools/technologies
    learning_order = models.JSONField()  # Ordered list of topics to learn
    estimated_duration = models.CharField(max_length=50, default="6-12 months")
    
    def __str__(self):
        return self.title
