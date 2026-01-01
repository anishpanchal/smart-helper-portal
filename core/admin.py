from django.contrib import admin
from .models import Subject, Note, StudyPlan, Notice, PlacementRoadmap


@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    list_display = ['name', 'code', 'semester']
    list_filter = ['semester']
    search_fields = ['name', 'code']


@admin.register(Note)
class NoteAdmin(admin.ModelAdmin):
    list_display = ['title', 'subject', 'uploaded_by', 'uploaded_at', 'download_count']
    list_filter = ['subject__semester', 'uploaded_at']
    search_fields = ['title', 'subject__name']


@admin.register(StudyPlan)
class StudyPlanAdmin(admin.ModelAdmin):
    list_display = ['user', 'course_name', 'exam_date', 'hours_per_day', 'is_completed', 'created_at']
    list_filter = ['is_completed', 'created_at']
    search_fields = ['user__username', 'course_name']


@admin.register(Notice)
class NoticeAdmin(admin.ModelAdmin):
    list_display = ['title', 'posted_by', 'posted_at', 'is_important']
    list_filter = ['is_important', 'posted_at']
    search_fields = ['title', 'content']


@admin.register(PlacementRoadmap)
class PlacementRoadmapAdmin(admin.ModelAdmin):
    list_display = ['title', 'career_path', 'estimated_duration']
    list_filter = ['career_path']
