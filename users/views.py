"""
Authentication views for Smart College Helper Portal
Handles signup, login, and logout
"""
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.views.decorators.http import require_http_methods
from .models import User, StudentProfile


def signup_view(request):
    """
    Student signup view
    """
    if request.user.is_authenticated:
        return redirect('core:dashboard')
    
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        password2 = request.POST.get('password2')
        phone = request.POST.get('phone', '')
        semester = request.POST.get('semester', 1)
        branch = request.POST.get('branch', '')
        
        # Validation
        if password != password2:
            messages.error(request, "Passwords don't match!")
            return render(request, 'users/signup.html')
        
        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists!")
            return render(request, 'users/signup.html')
        
        if User.objects.filter(email=email).exists():
            messages.error(request, "Email already registered!")
            return render(request, 'users/signup.html')
        
        # Create user
        try:
            user = User.objects.create_user(
                username=username,
                email=email,
                password=password,
                role='student',
                phone=phone
            )
            
            # Create student profile
            StudentProfile.objects.create(
                user=user,
                semester=int(semester),
                branch=branch
            )
            
            messages.success(request, "Account created successfully! Please login.")
            return redirect('users:login')
        except Exception as e:
            messages.error(request, f"Error creating account: {str(e)}")
    
    return render(request, 'users/signup.html')


def login_view(request):
    """
    User login view
    """
    if request.user.is_authenticated:
        return redirect('core:dashboard')
    
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            messages.success(request, f"Welcome back, {user.username}!")
            return redirect('core:dashboard')
        else:
            messages.error(request, "Invalid username or password!")
    
    return render(request, 'users/login.html')


@login_required
def logout_view(request):
    """
    User logout view
    """
    from django.contrib.auth import logout
    logout(request)
    messages.success(request, "You have been logged out successfully!")
    return redirect('users:login')
