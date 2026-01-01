"""
Management command to add sample college notes
Run: python manage.py add_sample_notes
"""
from django.core.management.base import BaseCommand
from core.models import Subject, Note
from users.models import User


class Command(BaseCommand):
    help = 'Adds sample college notes to the database'

    def handle(self, *args, **options):
        self.stdout.write('Adding sample notes...')
        
        # Get or create an admin user for uploading notes
        admin_user, created = User.objects.get_or_create(
            username='admin',
            defaults={
                'email': 'admin@example.com',
                'role': 'admin',
                'is_staff': True,
                'is_superuser': True
            }
        )
        
        if created:
            admin_user.set_password('admin123')
            admin_user.save()
            self.stdout.write('Created admin user for notes')
        
        # Sample notes data
        sample_notes = [
            {
                'title': 'DBMS Complete Notes - Chapter 1 to 5',
                'subject_code': 'DBMS',
                'semester': 3,
                'description': 'Complete notes covering Introduction to Database, ER Model, Relational Model, SQL Basics, and Normalization.'
            },
            {
                'title': 'Data Structures - Arrays and Linked Lists',
                'subject_code': 'DSA',
                'semester': 2,
                'description': 'Detailed notes on Arrays, Linked Lists, Stacks, and Queues with examples and algorithms.'
            },
            {
                'title': 'Web Development - HTML, CSS, JavaScript',
                'subject_code': 'WEB',
                'semester': 4,
                'description': 'Complete frontend development notes covering HTML5, CSS3, JavaScript ES6+, and DOM manipulation.'
            },
            {
                'title': 'Python Programming - Basics to Advanced',
                'subject_code': 'PYTHON',
                'semester': 2,
                'description': 'Comprehensive Python notes from basics to advanced topics including OOP, file handling, and modules.'
            },
            {
                'title': 'Machine Learning Fundamentals',
                'subject_code': 'ML',
                'semester': 5,
                'description': 'Introduction to Machine Learning, Supervised Learning, Unsupervised Learning, and Neural Networks basics.'
            },
            {
                'title': 'Operating Systems - Process Management',
                'subject_code': 'OS',
                'semester': 4,
                'description': 'Notes on Process Management, CPU Scheduling, Deadlocks, and Memory Management in Operating Systems.'
            },
            {
                'title': 'Computer Networks - OSI Model and TCP/IP',
                'subject_code': 'CN',
                'semester': 5,
                'description': 'Complete notes on Network Layers, Protocols, TCP/IP Model, Routing, and Network Security basics.'
            },
            {
                'title': 'Software Engineering - SDLC and Agile',
                'subject_code': 'SE',
                'semester': 6,
                'description': 'Software Development Life Cycle, Agile Methodology, UML Diagrams, and Software Testing concepts.'
            },
            {
                'title': 'DBMS - Advanced SQL Queries',
                'subject_code': 'DBMS',
                'semester': 3,
                'description': 'Advanced SQL topics including Joins, Subqueries, Views, Stored Procedures, and Triggers.'
            },
            {
                'title': 'Data Structures - Trees and Graphs',
                'subject_code': 'DSA',
                'semester': 2,
                'description': 'Binary Trees, BST, AVL Trees, Graph representation, BFS, DFS, and Graph Algorithms.'
            },
        ]
        
        notes_created = 0
        notes_skipped = 0
        
        for note_data in sample_notes:
            try:
                # Get the subject
                subject = Subject.objects.get(code=note_data['subject_code'])
                
                # Check if note already exists
                if Note.objects.filter(title=note_data['title'], subject=subject).exists():
                    self.stdout.write(self.style.WARNING(f'Note already exists: {note_data["title"]}'))
                    notes_skipped += 1
                    continue
                
                # Create a placeholder file path (in real scenario, you'd upload actual files)
                # For now, we'll create notes without files, or you can add actual PDF files later
                note = Note.objects.create(
                    title=note_data['title'],
                    subject=subject,
                    description=note_data['description'],
                    uploaded_by=admin_user,
                    # Note: file field is required, so we need to handle this
                    # For demo purposes, we'll skip file creation and let admin upload files manually
                )
                
                # Since file is required, we'll create a text file as placeholder
                from django.core.files.base import ContentFile
                file_content = f"Sample Notes: {note_data['title']}\n\n{note_data['description']}\n\nThis is a placeholder file. Please upload actual notes through the admin panel."
                note.file.save(
                    f"{note_data['subject_code']}_{note_data['title'][:20].replace(' ', '_')}.txt",
                    ContentFile(file_content.encode()),
                    save=True
                )
                
                notes_created += 1
                self.stdout.write(self.style.SUCCESS(f'Created note: {note_data["title"]}'))
                
            except Subject.DoesNotExist:
                self.stdout.write(self.style.ERROR(f'Subject not found: {note_data["subject_code"]}'))
            except Exception as e:
                self.stdout.write(self.style.ERROR(f'Error creating note {note_data["title"]}: {str(e)}'))
        
        self.stdout.write(self.style.SUCCESS(f'\nCreated {notes_created} notes'))
        if notes_skipped > 0:
            self.stdout.write(self.style.WARNING(f'Skipped {notes_skipped} duplicate notes'))
        self.stdout.write('\nNote: These are placeholder notes. You can upload actual PDF/DOCX files through the admin panel.')

