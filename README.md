# 🎓 Smart College Helper Portal

A production-ready, hackathon-winning web application that serves as an AI-powered digital assistant for college students. Built with Django, featuring modern UI with glassmorphism design, dark mode, and smooth animations.

## ✨ Features

### 🔐 Authentication System
- Student Signup / Login
- Role-based access (Student / Admin)
- Secure session-based authentication

### 🤖 AI Dashboard
- Personalized welcome message
- Animated dashboard cards:
  - Attendance Tracker
  - Assignment Reminder
  - Upcoming Events
  - Placement Status
- Premium, futuristic design

### 💬 Smart AI Assistant (Key Feature)
- ChatGPT-like chat interface
- Rule-based intelligent responses (no external API needed)
- Handles queries like:
  - "What should I study today?"
  - "Explain DBMS normalization"
  - "Suggest hackathon ideas"
  - "Give exam preparation roadmap"
- Typing animations and AI thinking loader

### 📅 Study Planner (AI Feature)
- Input: Course name, available hours per day, exam date
- Output: Auto-generated day-wise study plan
- Save plans to database
- Clean card layout display

### 📚 Notes & Resources Hub
- Admin can upload notes
- Students can view and download PDFs
- Filter by subject & semester

### 🚀 Placement & Skill Guidance
- Career roadmap cards:
  - Data Analyst
  - AI/ML Engineer
  - Web Developer
  - Software Engineer
  - Cybersecurity Specialist
- Each roadmap includes:
  - Required skills
  - Tools & technologies
  - Learning order
  - Estimated duration

### ⚙️ Admin Panel (Custom)
- Upload notices
- Upload notes
- View statistics
- View AI queries asked by students

### 🎨 UI/UX Features
- Dark mode (default)
- Glassmorphism design
- Smooth hover animations
- Animated buttons
- Loader animation on page load
- Mobile responsive design

## 🛠️ Tech Stack

- **Backend**: Django 4.2 + Django REST Framework
- **Frontend**: HTML, CSS, JavaScript (Modern UI)
- **Database**: SQLite (easy for hackathon)
- **Authentication**: Django Auth (Login / Signup)
- **AI Logic**: Rule-based + AI-ready architecture
- **Styling**: Glassmorphism + Dark Mode
- **Animations**: CSS + JS (smooth, professional)

## 📦 Installation & Setup

### Prerequisites
- Python 3.9 or higher
- pip (Python package manager)

### Step 1: Clone/Navigate to Project
```bash
cd randomproject/randomproject
```

### Step 2: Create Virtual Environment (if not already created)
```bash
# Windows
python -m venv venv
venv\Scripts\activate

# Linux/Mac
python3 -m venv venv
source venv/bin/activate
```

### Step 3: Install Dependencies
```bash
pip install django
```

### Step 4: Run Migrations
```bash
python manage.py makemigrations
python manage.py migrate
```

### Step 5: Create Superuser (Admin Account)
```bash
python manage.py createsuperuser
```
Follow the prompts to create an admin account.

### Step 6: Populate Initial Data
```bash
python manage.py init_data
```
This will create:
- Sample subjects (DBMS, DSA, Web Development, etc.)
- Placement roadmaps (Data Analyst, AI/ML Engineer, Web Developer, etc.)

### Step 7: Run Development Server
```bash
python manage.py runserver
```

### Step 8: Access the Application
- Open your browser and go to: `http://127.0.0.1:8000/`
- Sign up as a student or login with admin credentials

## 📁 Project Structure

```
randomproject/
├── manage.py
├── randomproject/
│   ├── settings.py
│   ├── urls.py
│   └── ...
├── core/
│   ├── models.py          # Notes, Study Plans, Notices, Roadmaps
│   ├── views.py           # Dashboard, Notes, Study Planner, etc.
│   ├── urls.py
│   ├── admin.py
│   └── management/
│       └── commands/
│           └── init_data.py
├── users/
│   ├── models.py          # User, StudentProfile
│   ├── views.py           # Signup, Login, Logout
│   └── urls.py
├── ai_helper/
│   ├── models.py          # AIQuery
│   ├── views.py           # AI Assistant
│   ├── ai_logic.py        # Rule-based AI responses
│   └── urls.py
├── templates/
│   ├── base.html
│   ├── users/
│   ├── core/
│   └── ai_helper/
├── static/
│   ├── css/
│   │   └── style.css      # Glassmorphism + Dark Mode
│   └── js/
│       └── main.js        # Animations & Interactions
└── media/                 # Uploaded files (notes, notices)
```

## 🎯 Usage Guide

### For Students:
1. **Sign Up**: Create a new account with your details
2. **Dashboard**: View your attendance, assignments, and upcoming events
3. **AI Assistant**: Ask questions about studies, exams, or career guidance
4. **Study Planner**: Create personalized study plans for your exams
5. **Notes**: Browse and download study materials
6. **Placement Guidance**: Explore career paths and skill roadmaps

### For Admins:
1. **Login**: Use your admin credentials
2. **Admin Panel**: Access from navigation menu
3. **Upload Notes**: Go to Admin Panel → Upload Note
4. **Post Notices**: Go to Admin Panel → Post Notice
5. **View Analytics**: See student statistics and AI queries

## 🚀 Hackathon Pitch Points

### Problem Statement:
College students struggle with:
- Managing study schedules
- Finding relevant study materials
- Getting instant academic help
- Career guidance and placement preparation

### Solution:
Smart College Helper Portal - An AI-powered platform that:
- Provides 24/7 AI assistance for academic queries
- Generates personalized study plans
- Centralizes study materials
- Offers career guidance with detailed roadmaps

### Key Differentiators:
1. **No External API Dependency**: Rule-based AI works offline
2. **Modern UI**: Glassmorphism design stands out
3. **Complete Solution**: All-in-one platform
4. **Production Ready**: Clean code, proper structure, scalable

### Future Enhancements:
- Integration with real AI APIs (OpenAI, etc.)
- Mobile app version
- Real-time notifications
- Collaborative study groups
- Integration with college LMS

## 🐛 Troubleshooting

### Issue: Static files not loading
**Solution**: Run `python manage.py collectstatic` (if needed)

### Issue: Media files not accessible
**Solution**: Ensure `MEDIA_ROOT` and `MEDIA_URL` are set correctly in settings.py

### Issue: Migration errors
**Solution**: 
```bash
python manage.py makemigrations
python manage.py migrate
```

### Issue: Admin panel not accessible
**Solution**: Create superuser with `python manage.py createsuperuser`

## 📝 Notes

- The AI assistant uses rule-based logic (no external APIs)
- All data is stored in SQLite database
- File uploads are stored in `media/` directory
- The application is ready for hackathon demo

## 👨‍💻 Development

### Adding New AI Responses:
Edit `ai_helper/ai_logic.py` and add new response patterns in the `SmartAIAssistant` class.

### Adding New Models:
1. Add model in respective `models.py`
2. Run `python manage.py makemigrations`
3. Run `python manage.py migrate`
4. Register in `admin.py`

### Customizing UI:
- Main styles: `static/css/style.css`
- JavaScript: `static/js/main.js`
- Base template: `templates/base.html`

## 📄 License

This project is created for hackathon purposes. Feel free to use and modify.

## 🙏 Acknowledgments

- Built with Django
- UI inspired by modern glassmorphism design
- Icons from Font Awesome

---

**Built with ❤️ for Smart College Students**

For questions or issues, check the code comments or Django documentation.

