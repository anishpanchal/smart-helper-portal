"""
URL configuration for ai_helper app
"""
from django.urls import path
from . import views

app_name = 'ai_helper'

urlpatterns = [
    path('', views.ai_assistant_view, name='ai_assistant'),
    path('api/query/', views.ai_query_api, name='ai_query_api'),
]

