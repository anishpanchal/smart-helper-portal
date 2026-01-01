# 🚀 Quick Start Guide

## Setup in 5 Minutes

### 1. Navigate to Project
```bash
cd randomproject/randomproject
```

### 2. Activate Virtual Environment
```bash
# Windows
venv\Scripts\activate

# Linux/Mac  
source ../venv/bin/activate
```

### 3. Install Django (if not installed)
```bash
pip install django
```

### 4. Run Migrations
```bash
python manage.py makemigrations
python manage.py migrate
```

### 5. Create Admin User
```bash
python manage.py createsuperuser
# Enter username, email, and password when prompted
```

### 6. Populate Initial Data
```bash
python manage.py init_data
```

### 7. Run Server
```bash
python manage.py runserver
```

### 8. Open Browser
Go to: **http://127.0.0.1:8000/**

## First Steps

1. **Sign Up** as a student at `/users/signup/`
2. **Login** and explore the dashboard
3. **Try AI Assistant** at `/ai-assistant/`
4. **Create Study Plan** at `/study-planner/`
5. **Login as Admin** to upload notes and notices

## Default Admin Access

- URL: `/admin/`
- Use the superuser credentials you created

## Key Features to Demo

✅ **AI Assistant** - Ask "What should I study today?"
✅ **Study Planner** - Create a study plan for an exam
✅ **Dashboard** - View animated cards
✅ **Placement Guidance** - Explore career roadmaps
✅ **Notes Hub** - Upload and download notes (admin)

## Troubleshooting

**Static files not loading?**
- Check that `static/` folder exists
- Run: `python manage.py collectstatic` (if needed)

**Can't access admin?**
- Make sure you created superuser: `python manage.py createsuperuser`

**Migration errors?**
- Delete `db.sqlite3` and run migrations again

---

**Ready to win that hackathon! 🏆**

