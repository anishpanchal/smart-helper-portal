"""
User models for Smart College Helper Portal
Extended User model with role-based access
"""
from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    """
    Extended User model with role field
    Roles: 'student' or 'admin'
    """
    ROLE_CHOICES = [
        ('student', 'Student'),
        ('admin', 'Admin'),
    ]
    
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='student')
    phone = models.CharField(max_length=15, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.username} ({self.role})"
    
    def is_student(self):
        return self.role == 'student'
    
    def is_admin(self):
        return self.role == 'admin'


class StudentProfile(models.Model):
    """
    Additional profile information for students
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='student_profile')
    enrollment_number = models.CharField(max_length=50, unique=True, blank=True, null=True)
    semester = models.IntegerField(default=1)
    branch = models.CharField(max_length=100, blank=True, null=True)
    attendance_percentage = models.FloatField(default=0.0)
    assignments_completed = models.IntegerField(default=0)
    assignments_pending = models.IntegerField(default=0)
    
    def __str__(self):
        return f"{self.user.username} - Semester {self.semester}"
