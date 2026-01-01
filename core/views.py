"""
Core views for Smart College Helper Portal
Dashboard, Notes, Study Planner, Placement Guidance, Admin Panel
"""
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import JsonResponse, FileResponse
from django.utils import timezone
from datetime import datetime, timedelta
import json

from .models import Note, StudyPlan, Notice, PlacementRoadmap, Subject
from users.models import StudentProfile, User
from ai_helper.models import AIQuery


@login_required
def dashboard_view(request):
    """
    Main dashboard with animated cards and student info
    """
    user = request.user
    
    # Get student profile if exists
    try:
        profile = user.student_profile
    except:
        profile = None
    
    # Get upcoming events (notices)
    upcoming_notices = Notice.objects.all()[:5]
    
    # Get recent study plans
    recent_plans = StudyPlan.objects.filter(user=user)[:3]
    
    # Calculate days until next exam (if study plan exists)
    next_exam = None
    days_until_exam = None
    if recent_plans.exists():
        next_plan = recent_plans.first()
        if next_plan.exam_date:
            days_until_exam = (next_plan.exam_date - timezone.now().date()).days
            next_exam = next_plan
    
    context = {
        'user': user,
        'profile': profile,
        'upcoming_notices': upcoming_notices,
        'recent_plans': recent_plans,
        'next_exam': next_exam,
        'days_until_exam': days_until_exam,
    }
    
    return render(request, 'core/dashboard.html', context)


@login_required
def attendance_view(request):
    """
    Detailed attendance view for students
    """
    user = request.user
    
    # Get student profile if exists
    try:
        profile = user.student_profile
    except:
        profile = None
    
    # Calculate attendance statistics
    attendance_percentage = profile.attendance_percentage if profile else 85.0
    is_eligible = attendance_percentage >= 75
    
    # Calculate how many classes can be missed
    # Assuming 100 total classes (can be made dynamic)
    total_classes = 100
    
    if profile:
        attended_classes = int((attendance_percentage / 100) * total_classes)
        missed_classes = total_classes - attended_classes
        classes_remaining = total_classes - attended_classes
        max_missable = int((0.25 * total_classes))  # 25% can be missed
        can_miss = max(0, max_missable - missed_classes)
    else:
        attended_classes = 85
        missed_classes = 15
        classes_remaining = 15
        can_miss = 10
    
    # Calculate classes needed to reach 75%
    if attendance_percentage < 75:
        # To reach 75%, need: (0.75 * total_classes) - attended_classes
        classes_needed = max(0, int(0.75 * total_classes) - attended_classes)
    else:
        classes_needed = 0
    
    context = {
        'user': user,
        'profile': profile,
        'attendance_percentage': attendance_percentage,
        'is_eligible': is_eligible,
        'total_classes': total_classes,
        'attended_classes': attended_classes,
        'missed_classes': missed_classes,
        'classes_remaining': classes_remaining,
        'can_miss': can_miss,
        'classes_needed': classes_needed,
        'target_percentage': 75,
    }
    
    return render(request, 'core/attendance.html', context)


@login_required
def notes_view(request):
    """
    Notes and Resources Hub
    """
    notes = Note.objects.all()
    subjects = Subject.objects.all()
    semester_filter = request.GET.get('semester')
    subject_filter = request.GET.get('subject')
    
    if semester_filter:
        notes = notes.filter(subject__semester=semester_filter)
    
    if subject_filter:
        notes = notes.filter(subject_id=subject_filter)
    
    context = {
        'notes': notes,
        'subjects': subjects,
        'selected_semester': semester_filter,
        'selected_subject': subject_filter,
    }
    
    return render(request, 'core/notes.html', context)


@login_required
def download_note(request, note_id):
    """
    Download note file
    """
    note = get_object_or_404(Note, id=note_id)
    note.download_count += 1
    note.save()
    
    return FileResponse(open(note.file.path, 'rb'), as_attachment=True, filename=note.file.name)


@login_required
def study_planner_view(request):
    """
    Study Planner - Create and view study plans
    """
    if request.method == 'POST':
        course_name = request.POST.get('course_name')
        exam_date_str = request.POST.get('exam_date')
        hours_per_day = int(request.POST.get('hours_per_day', 2))
        
        try:
            exam_date = datetime.strptime(exam_date_str, '%Y-%m-%d').date()
            days_until_exam = (exam_date - timezone.now().date()).days
            
            if days_until_exam <= 0:
                messages.error(request, "Exam date must be in the future!")
                return redirect('core:study_planner')
            
            # Generate study plan
            plan_data = generate_study_plan(course_name, days_until_exam, hours_per_day)
            
            # Save study plan
            study_plan = StudyPlan.objects.create(
                user=request.user,
                course_name=course_name,
                exam_date=exam_date,
                hours_per_day=hours_per_day,
                plan_data=plan_data
            )
            
            messages.success(request, "Study plan created successfully!")
            return redirect('core:study_planner')
        except Exception as e:
            messages.error(request, f"Error creating study plan: {str(e)}")
    
    # Get user's study plans
    study_plans = StudyPlan.objects.filter(user=request.user).order_by('-created_at')
    
    context = {
        'study_plans': study_plans,
    }
    
    return render(request, 'core/study_planner.html', context)


def generate_study_plan(course_name, days, hours_per_day):
    """
    Generate day-wise study plan
    """
    plan = []
    total_hours = days * hours_per_day
    
    # Divide into phases
    phase1_days = days // 3  # Learning phase
    phase2_days = days // 3  # Practice phase
    phase3_days = days - phase1_days - phase2_days  # Revision phase
    
    current_date = timezone.now().date()
    
    # Phase 1: Learning
    for i in range(phase1_days):
        plan.append({
            'day': i + 1,
            'date': str(current_date + timedelta(days=i)),
            'phase': 'Learning',
            'tasks': [
                f"Study {course_name} fundamentals",
                "Read textbook chapters",
                "Watch video lectures",
                "Take notes on key concepts"
            ],
            'hours': hours_per_day
        })
    
    # Phase 2: Practice
    for i in range(phase2_days):
        plan.append({
            'day': phase1_days + i + 1,
            'date': str(current_date + timedelta(days=phase1_days + i)),
            'phase': 'Practice',
            'tasks': [
                "Solve practice problems",
                "Complete assignments",
                "Take mock tests",
                "Review previous topics"
            ],
            'hours': hours_per_day
        })
    
    # Phase 3: Revision
    for i in range(phase3_days):
        plan.append({
            'day': phase1_days + phase2_days + i + 1,
            'date': str(current_date + timedelta(days=phase1_days + phase2_days + i)),
            'phase': 'Revision',
            'tasks': [
                "Quick revision of all topics",
                "Review notes and formulas",
                "Solve previous year papers",
                "Final preparation"
            ],
            'hours': hours_per_day
        })
    
    return plan


@login_required
def placement_guidance_view(request):
    """
    Placement & Skill Guidance with roadmaps
    """
    roadmaps = PlacementRoadmap.objects.all()
    
    context = {
        'roadmaps': roadmaps,
    }
    
    return render(request, 'core/placement_guidance.html', context)


@login_required
def admin_panel_view(request):
    """
    Custom admin panel for managing content
    """
    if not request.user.is_admin():
        messages.error(request, "Access denied! Admin only.")
        return redirect('core:dashboard')
    
    # Get statistics
    total_students = User.objects.filter(role='student').count()
    total_notes = Note.objects.count()
    total_notices = Notice.objects.count()
    total_queries = AIQuery.objects.count()
    
    # Get recent AI queries
    recent_queries = AIQuery.objects.all()[:10]
    
    context = {
        'total_students': total_students,
        'total_notes': total_notes,
        'total_notices': total_notices,
        'total_queries': total_queries,
        'recent_queries': recent_queries,
    }
    
    return render(request, 'core/admin_panel.html', context)


@login_required
def admin_upload_note(request):
    """
    Admin upload note
    """
    if not request.user.is_admin():
        messages.error(request, "Access denied!")
        return redirect('core:dashboard')
    
    if request.method == 'POST':
        title = request.POST.get('title')
        subject_id = request.POST.get('subject')
        file = request.FILES.get('file')
        description = request.POST.get('description', '')
        
        try:
            subject = Subject.objects.get(id=subject_id)
            Note.objects.create(
                title=title,
                subject=subject,
                file=file,
                description=description,
                uploaded_by=request.user
            )
            messages.success(request, "Note uploaded successfully!")
        except Exception as e:
            messages.error(request, f"Error: {str(e)}")
    
    subjects = Subject.objects.all()
    context = {'subjects': subjects}
    return render(request, 'core/admin_upload_note.html', context)


@login_required
def admin_upload_notice(request):
    """
    Admin upload notice
    """
    if not request.user.is_admin():
        messages.error(request, "Access denied!")
        return redirect('core:dashboard')
    
    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')
        file = request.FILES.get('file', None)
        is_important = request.POST.get('is_important') == 'on'
        
        try:
            Notice.objects.create(
                title=title,
                content=content,
                file=file,
                is_important=is_important,
                posted_by=request.user
            )
            messages.success(request, "Notice posted successfully!")
        except Exception as e:
            messages.error(request, f"Error: {str(e)}")
    
    return render(request, 'core/admin_upload_notice.html')
