"""
URL configuration for core app
"""
from django.urls import path
from . import views

app_name = 'core'

urlpatterns = [
    path('', views.dashboard_view, name='dashboard'),
    path('attendance/', views.attendance_view, name='attendance'),
    path('notes/', views.notes_view, name='notes'),
    path('notes/<int:note_id>/download/', views.download_note, name='download_note'),
    path('study-planner/', views.study_planner_view, name='study_planner'),
    path('placement-guidance/', views.placement_guidance_view, name='placement_guidance'),
    path('admin-panel/', views.admin_panel_view, name='admin_panel'),
    path('admin-panel/upload-note/', views.admin_upload_note, name='admin_upload_note'),
    path('admin-panel/upload-notice/', views.admin_upload_notice, name='admin_upload_notice'),
]

