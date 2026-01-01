"""
Management command to populate initial data
Run: python manage.py init_data
"""
from django.core.management.base import BaseCommand
from core.models import Subject, PlacementRoadmap


class Command(BaseCommand):
    help = 'Populates initial data (Subjects and Placement Roadmaps)'

    def handle(self, *args, **options):
        self.stdout.write('Creating initial data...')
        
        # Create Subjects
        subjects_data = [
            {'name': 'Database Management Systems', 'code': 'DBMS', 'semester': 3},
            {'name': 'Data Structures and Algorithms', 'code': 'DSA', 'semester': 2},
            {'name': 'Web Development', 'code': 'WEB', 'semester': 4},
            {'name': 'Python Programming', 'code': 'PYTHON', 'semester': 2},
            {'name': 'Machine Learning', 'code': 'ML', 'semester': 5},
            {'name': 'Operating Systems', 'code': 'OS', 'semester': 4},
            {'name': 'Computer Networks', 'code': 'CN', 'semester': 5},
            {'name': 'Software Engineering', 'code': 'SE', 'semester': 6},
        ]
        
        for subj_data in subjects_data:
            subject, created = Subject.objects.get_or_create(
                code=subj_data['code'],
                defaults=subj_data
            )
            if created:
                self.stdout.write(self.style.SUCCESS(f'Created subject: {subject.name}'))
            else:
                self.stdout.write(self.style.WARNING(f'Subject already exists: {subject.name}'))
        
        # Create Placement Roadmaps
        roadmaps_data = [
            {
                'career_path': 'data_analyst',
                'title': 'Data Analyst Career Path',
                'description': 'Become a skilled data analyst who can extract insights from data and help businesses make data-driven decisions.',
                'skills': [
                    'SQL and Database Management',
                    'Data Visualization (Tableau, Power BI)',
                    'Statistical Analysis',
                    'Excel Advanced Functions',
                    'Python/R for Data Analysis',
                    'Problem-Solving Skills'
                ],
                'tools': [
                    'SQL (MySQL, PostgreSQL)',
                    'Python (Pandas, NumPy)',
                    'Tableau / Power BI',
                    'Excel',
                    'Jupyter Notebooks',
                    'Git'
                ],
                'learning_order': [
                    'Learn SQL fundamentals and practice queries',
                    'Master Excel for data manipulation',
                    'Learn Python basics and Pandas library',
                    'Practice data visualization with Tableau/Power BI',
                    'Study statistics and data analysis techniques',
                    'Build portfolio projects with real datasets',
                    'Prepare for interviews with case studies'
                ],
                'estimated_duration': '6-8 months'
            },
            {
                'career_path': 'ai_ml_engineer',
                'title': 'AI/ML Engineer Career Path',
                'description': 'Master artificial intelligence and machine learning to build intelligent systems and predictive models.',
                'skills': [
                    'Python Programming',
                    'Machine Learning Algorithms',
                    'Deep Learning (Neural Networks)',
                    'Data Preprocessing',
                    'Model Deployment',
                    'Mathematics (Linear Algebra, Calculus)'
                ],
                'tools': [
                    'Python (NumPy, Pandas, Scikit-learn)',
                    'TensorFlow / PyTorch',
                    'Jupyter Notebooks',
                    'Docker',
                    'Cloud Platforms (AWS, GCP)',
                    'Git & GitHub'
                ],
                'learning_order': [
                    'Master Python programming fundamentals',
                    'Learn mathematics (Linear Algebra, Statistics)',
                    'Study machine learning basics and algorithms',
                    'Practice with Scikit-learn library',
                    'Learn deep learning with TensorFlow/PyTorch',
                    'Work on real ML projects',
                    'Learn model deployment and MLOps',
                    'Build a strong portfolio'
                ],
                'estimated_duration': '8-12 months'
            },
            {
                'career_path': 'web_developer',
                'title': 'Web Developer Career Path',
                'description': 'Build modern, responsive web applications using frontend and backend technologies.',
                'skills': [
                    'HTML, CSS, JavaScript',
                    'Frontend Framework (React/Vue/Angular)',
                    'Backend Development (Node.js/Django)',
                    'Database Management',
                    'RESTful APIs',
                    'Version Control (Git)'
                ],
                'tools': [
                    'React / Vue.js / Angular',
                    'Node.js / Django / Flask',
                    'MongoDB / PostgreSQL',
                    'VS Code',
                    'Git & GitHub',
                    'Postman'
                ],
                'learning_order': [
                    'Master HTML, CSS, and JavaScript fundamentals',
                    'Learn a frontend framework (React recommended)',
                    'Study backend development (Node.js or Django)',
                    'Learn database design and SQL/NoSQL',
                    'Build RESTful APIs',
                    'Practice with full-stack projects',
                    'Learn deployment (Heroku, AWS, Vercel)',
                    'Create a portfolio website'
                ],
                'estimated_duration': '6-10 months'
            },
            {
                'career_path': 'software_engineer',
                'title': 'Software Engineer Career Path',
                'description': 'Become a versatile software engineer capable of building scalable applications and systems.',
                'skills': [
                    'Programming Languages (Java/Python/C++)',
                    'Data Structures & Algorithms',
                    'System Design',
                    'Software Development Life Cycle',
                    'Testing & Debugging',
                    'Problem-Solving'
                ],
                'tools': [
                    'Java / Python / C++',
                    'Git & GitHub',
                    'Docker & Kubernetes',
                    'CI/CD Tools',
                    'IDEs (IntelliJ, VS Code)',
                    'Jira / Trello'
                ],
                'learning_order': [
                    'Master at least one programming language',
                    'Study data structures and algorithms thoroughly',
                    'Practice coding problems (LeetCode, HackerRank)',
                    'Learn system design principles',
                    'Build projects using best practices',
                    'Learn version control and collaboration tools',
                    'Prepare for technical interviews',
                    'Contribute to open-source projects'
                ],
                'estimated_duration': '8-12 months'
            },
            {
                'career_path': 'cybersecurity',
                'title': 'Cybersecurity Specialist Career Path',
                'description': 'Protect systems and networks from cyber threats and ensure data security.',
                'skills': [
                    'Network Security',
                    'Ethical Hacking',
                    'Cryptography',
                    'Security Auditing',
                    'Incident Response',
                    'Risk Assessment'
                ],
                'tools': [
                    'Wireshark',
                    'Metasploit',
                    'Nmap',
                    'Burp Suite',
                    'Kali Linux',
                    'SIEM Tools'
                ],
                'learning_order': [
                    'Learn networking fundamentals',
                    'Study cybersecurity basics and threats',
                    'Learn ethical hacking and penetration testing',
                    'Practice with security tools (Wireshark, Nmap)',
                    'Study cryptography and encryption',
                    'Get certified (CEH, Security+)',
                    'Practice on platforms like HackTheBox',
                    'Build security projects and portfolio'
                ],
                'estimated_duration': '10-14 months'
            },
        ]
        
        for roadmap_data in roadmaps_data:
            roadmap, created = PlacementRoadmap.objects.get_or_create(
                career_path=roadmap_data['career_path'],
                defaults=roadmap_data
            )
            if created:
                self.stdout.write(self.style.SUCCESS(f'Created roadmap: {roadmap.title}'))
            else:
                self.stdout.write(self.style.WARNING(f'Roadmap already exists: {roadmap.title}'))
        
        self.stdout.write(self.style.SUCCESS('\nInitial data populated successfully!'))

