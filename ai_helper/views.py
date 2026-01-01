"""
AI Helper views for Smart College Helper Portal
Handles AI chat interface and responses
"""
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
import json

from .models import AIQuery
from .ai_logic import SmartAIAssistant


@login_required
def ai_assistant_view(request):
    """
    AI Assistant chat interface
    """
    # Get recent queries for this user
    recent_queries = AIQuery.objects.filter(user=request.user)[:10]
    
    context = {
        'recent_queries': recent_queries,
    }
    
    return render(request, 'ai_helper/ai_assistant.html', context)


@login_required
@require_http_methods(["POST"])
def ai_query_api(request):
    """
    API endpoint for AI queries
    Returns JSON response
    """
    try:
        data = json.loads(request.body)
        query = data.get('query', '').strip()
        
        if not query:
            return JsonResponse({
                'success': False,
                'error': 'Query cannot be empty'
            })
        
        # Process query with AI
        ai = SmartAIAssistant()
        response = ai.process_query(query, user=request.user)
        
        # Save query and response
        ai_query = AIQuery.objects.create(
            user=request.user,
            query=query,
            response=response
        )
        
        return JsonResponse({
            'success': True,
            'response': response,
            'query_id': ai_query.id
        })
    
    except Exception as e:
        return JsonResponse({
            'success': False,
            'error': str(e)
        })
