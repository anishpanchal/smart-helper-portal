"""
AI Logic Module - Rule-based intelligent responses
No external API needed - Pure Python logic
"""
import re
import random
from datetime import datetime, timedelta


class SmartAIAssistant:
    """
    Rule-based AI Assistant for Smart College Helper Portal
    Provides intelligent responses based on keyword matching and context
    """
    
    def __init__(self):
        self.greetings = [
            "Hello! How can I help you today?",
            "Hi there! What would you like to know?",
            "Hey! I'm here to assist you with your college journey.",
        ]
        
        self.study_responses = {
            'today': self._get_study_today_response,
            'study': self._get_study_plan_response,
            'exam': self._get_exam_prep_response,
            'assignment': self._get_assignment_response,
        }
        
        self.explanation_keywords = {
            'dbms': self._explain_dbms,
            'normalization': self._explain_normalization,
            'sql': self._explain_sql,
            'python': self._explain_python,
            'javascript': self._explain_javascript,
            'algorithm': self._explain_algorithm,
            'data structure': self._explain_data_structure,
        }
        
        self.hackathon_responses = [
            "Great question! Here are some hackathon ideas:\n\n"
            "1. **Smart Attendance System** - Face recognition + GPS tracking\n"
            "2. **AI Study Buddy** - Personalized learning assistant\n"
            "3. **Campus Navigation App** - AR-based indoor navigation\n"
            "4. **Waste Management System** - IoT sensors for smart bins\n"
            "5. **Mental Health Tracker** - Mood analysis + counseling bot\n\n"
            "Choose one that solves a real problem and you're passionate about!",
            
            "Here are trending hackathon ideas:\n\n"
            "1. **Blockchain Voting System** - Secure & transparent\n"
            "2. **AI-Powered Resume Builder** - Auto-generate optimized resumes\n"
            "3. **Smart Library Management** - RFID + Mobile app\n"
            "4. **Carbon Footprint Calculator** - Track & reduce emissions\n"
            "5. **Virtual Lab Simulator** - Learn experiments remotely\n\n"
            "Focus on innovation and user experience!",
        ]
    
    def process_query(self, query, user=None):
        """
        Main method to process user query and return AI response
        """
        query_lower = query.lower().strip()
        
        # Check for greetings
        if any(word in query_lower for word in ['hi', 'hello', 'hey', 'good morning', 'good afternoon']):
            return random.choice(self.greetings)
        
        # Check for study-related queries
        if any(word in query_lower for word in ['study', 'what should i study', 'what to study']):
            if 'today' in query_lower:
                return self._get_study_today_response()
            return self._get_study_plan_response()
        
        # Check for exam preparation
        if any(word in query_lower for word in ['exam', 'examination', 'prepare', 'preparation']):
            return self._get_exam_prep_response()
        
        # Check for explanations
        for keyword, explain_func in self.explanation_keywords.items():
            if keyword in query_lower:
                return explain_func()
        
        # Check for hackathon ideas
        if any(word in query_lower for word in ['hackathon', 'project idea', 'idea', 'build']):
            return random.choice(self.hackathon_responses)
        
        # Check for assignment help
        if any(word in query_lower for word in ['assignment', 'homework', 'task']):
            return self._get_assignment_response()
        
        # Check for placement/career guidance
        if any(word in query_lower for word in ['placement', 'job', 'career', 'internship']):
            return self._get_placement_guidance()
        
        # Check for attendance
        if any(word in query_lower for word in ['attendance', 'present', 'absent']):
            return self._get_attendance_info()
        
        # Default intelligent response
        return self._get_default_response(query)
    
    def _get_study_today_response(self):
        """Generate study plan for today"""
        subjects = [
            "Database Management Systems (DBMS)",
            "Data Structures and Algorithms",
            "Web Development",
            "Python Programming",
            "Machine Learning Basics",
            "Operating Systems",
        ]
        
        selected = random.sample(subjects, 2)
        hours = random.randint(2, 4)
        
        return (
            f"📚 **Today's Study Plan**\n\n"
            f"Based on your academic schedule, I recommend focusing on:\n\n"
            f"1. **{selected[0]}** - {hours} hours\n"
            f"   - Review key concepts\n"
            f"   - Solve practice problems\n"
            f"   - Take notes on important topics\n\n"
            f"2. **{selected[1]}** - {hours-1} hours\n"
            f"   - Complete pending assignments\n"
            f"   - Watch tutorial videos\n"
            f"   - Practice coding exercises\n\n"
            f"💡 **Pro Tip**: Take 10-minute breaks every hour. Stay hydrated and maintain focus!"
        )
    
    def _get_study_plan_response(self):
        """General study planning advice"""
        return (
            "📖 **Smart Study Planning**\n\n"
            "Here's an effective study strategy:\n\n"
            "1. **Morning (6-9 AM)**: Focus on difficult subjects when your mind is fresh\n"
            "2. **Afternoon (2-5 PM)**: Practice problems and assignments\n"
            "3. **Evening (7-9 PM)**: Review and revise what you learned\n\n"
            "**Techniques to Try:**\n"
            "• Pomodoro Technique (25 min study + 5 min break)\n"
            "• Active Recall (test yourself without notes)\n"
            "• Spaced Repetition (review after 1 day, 3 days, 1 week)\n\n"
            "Would you like me to create a detailed study plan? Just provide:\n"
            "- Course name\n"
            "- Exam date\n"
            "- Hours available per day"
        )
    
    def _get_exam_prep_response(self):
        """Exam preparation roadmap"""
        return (
            "🎯 **Exam Preparation Roadmap**\n\n"
            "**4 Weeks Before Exam:**\n"
            "• Review all syllabus topics\n"
            "• Create summary notes\n"
            "• Identify weak areas\n\n"
            "**3 Weeks Before:**\n"
            "• Focus on weak topics\n"
            "• Solve previous year papers\n"
            "• Join study groups\n\n"
            "**2 Weeks Before:**\n"
            "• Daily revision of all topics\n"
            "• Mock tests\n"
            "• Time management practice\n\n"
            "**1 Week Before:**\n"
            "• Final revision only\n"
            "• Light study (4-5 hours/day)\n"
            "• Maintain sleep schedule\n"
            "• Stay calm and confident\n\n"
            "💪 You've got this! Consistency is key."
        )
    
    def _get_assignment_response(self):
        """Assignment help response"""
        return (
            "📝 **Assignment Help**\n\n"
            "Here's how to tackle assignments effectively:\n\n"
            "1. **Understand Requirements**: Read the assignment carefully\n"
            "2. **Plan Your Approach**: Break it into smaller tasks\n"
            "3. **Research**: Use textbooks, online resources, and notes\n"
            "4. **Start Early**: Don't wait until the last minute\n"
            "5. **Review**: Check for errors and formatting\n\n"
            "**Resources Available:**\n"
            "• Notes section in portal\n"
            "• Previous year solutions\n"
            "• Online tutorials and documentation\n\n"
            "If you need help with a specific topic, just ask me!"
        )
    
    def _get_placement_guidance(self):
        """Placement and career guidance"""
        return (
            "🚀 **Placement & Career Guidance**\n\n"
            "To excel in placements:\n\n"
            "**Technical Skills:**\n"
            "• Strong programming fundamentals\n"
            "• Data Structures & Algorithms\n"
            "• Problem-solving practice (LeetCode, HackerRank)\n\n"
            "**Soft Skills:**\n"
            "• Communication skills\n"
            "• Team collaboration\n"
            "• Leadership experience\n\n"
            "**Preparation Timeline:**\n"
            "• 6 months before: Build strong foundation\n"
            "• 3 months before: Start mock interviews\n"
            "• 1 month before: Final preparation & resume polish\n\n"
            "Check out the Placement & Skill Guidance section for detailed roadmaps!"
        )
    
    def _get_attendance_info(self):
        """Attendance information"""
        return (
            "📊 **Attendance Tracker**\n\n"
            "Maintaining good attendance is crucial:\n\n"
            "**Benefits:**\n"
            "• Better understanding of concepts\n"
            "• Direct interaction with professors\n"
            "• Eligibility for exams (usually 75% required)\n\n"
            "**Tips:**\n"
            "• Set daily reminders\n"
            "• Track your attendance regularly\n"
            "• Plan leaves strategically\n\n"
            "Check your dashboard for current attendance percentage!"
        )
    
    def _explain_dbms(self):
        """Explain DBMS concepts"""
        return (
            "🗄️ **Database Management System (DBMS)**\n\n"
            "**What is DBMS?**\n"
            "A software system that manages databases, allowing users to store, retrieve, and manipulate data efficiently.\n\n"
            "**Key Concepts:**\n"
            "• **Database**: Collection of related data\n"
            "• **Tables**: Organized data in rows and columns\n"
            "• **SQL**: Language to interact with databases\n"
            "• **ACID Properties**: Atomicity, Consistency, Isolation, Durability\n\n"
            "**Types:**\n"
            "1. Relational DBMS (MySQL, PostgreSQL)\n"
            "2. NoSQL (MongoDB, Cassandra)\n"
            "3. Object-oriented DBMS\n\n"
            "**Common Operations:**\n"
            "• CREATE, INSERT, SELECT, UPDATE, DELETE\n"
            "• JOIN operations for combining tables\n"
            "• Indexing for faster queries\n\n"
            "Would you like me to explain normalization or SQL queries in detail?"
        )
    
    def _explain_normalization(self):
        """Explain database normalization"""
        return (
            "📐 **Database Normalization**\n\n"
            "Normalization is the process of organizing data to reduce redundancy and improve data integrity.\n\n"
            "**Normal Forms:**\n\n"
            "**1NF (First Normal Form):**\n"
            "• Each column contains atomic values\n"
            "• No repeating groups\n\n"
            "**2NF (Second Normal Form):**\n"
            "• Must be in 1NF\n"
            "• All non-key attributes fully depend on primary key\n\n"
            "**3NF (Third Normal Form):**\n"
            "• Must be in 2NF\n"
            "• No transitive dependencies\n"
            "• Non-key attributes depend only on primary key\n\n"
            "**Benefits:**\n"
            "• Reduces data redundancy\n"
            "• Prevents update anomalies\n"
            "• Improves data integrity\n"
            "• Saves storage space\n\n"
            "**Example:**\n"
            "Instead of storing student name, course, and instructor in one table,\n"
            "split into: Students, Courses, Enrollments tables."
        )
    
    def _explain_sql(self):
        """Explain SQL basics"""
        return (
            "💾 **SQL (Structured Query Language)**\n\n"
            "SQL is used to communicate with databases.\n\n"
            "**Basic Commands:**\n\n"
            "**SELECT**: Retrieve data\n"
            "```sql\n"
            "SELECT * FROM students WHERE age > 20;\n"
            "```\n\n"
            "**INSERT**: Add new records\n"
            "```sql\n"
            "INSERT INTO students (name, age) VALUES ('John', 22);\n"
            "```\n\n"
            "**UPDATE**: Modify existing data\n"
            "```sql\n"
            "UPDATE students SET age = 23 WHERE name = 'John';\n"
            "```\n\n"
            "**DELETE**: Remove records\n"
            "```sql\n"
            "DELETE FROM students WHERE age < 18;\n"
            "```\n\n"
            "**JOIN**: Combine data from multiple tables\n"
            "```sql\n"
            "SELECT s.name, c.course_name\n"
            "FROM students s\n"
            "JOIN enrollments e ON s.id = e.student_id\n"
            "JOIN courses c ON e.course_id = c.id;\n"
            "```"
        )
    
    def _explain_python(self):
        """Explain Python basics"""
        return (
            "🐍 **Python Programming**\n\n"
            "Python is a high-level, interpreted programming language.\n\n"
            "**Key Features:**\n"
            "• Simple and readable syntax\n"
            "• Extensive libraries\n"
            "• Great for data science, web development, AI/ML\n\n"
            "**Basic Concepts:**\n"
            "• Variables and data types\n"
            "• Control structures (if/else, loops)\n"
            "• Functions and classes\n"
            "• File handling\n"
            "• Exception handling\n\n"
            "**Popular Libraries:**\n"
            "• NumPy, Pandas (Data Science)\n"
            "• Django, Flask (Web Development)\n"
            "• TensorFlow, PyTorch (Machine Learning)\n"
            "• Requests (HTTP library)\n\n"
            "Start with basics, then move to advanced topics!"
        )
    
    def _explain_javascript(self):
        """Explain JavaScript basics"""
        return (
            "⚡ **JavaScript**\n\n"
            "JavaScript is a programming language for web development.\n\n"
            "**Key Features:**\n"
            "• Client-side and server-side (Node.js)\n"
            "• Dynamic and interactive web pages\n"
            "• Event-driven programming\n\n"
            "**Core Concepts:**\n"
            "• Variables (let, const, var)\n"
            "• Functions and arrow functions\n"
            "• DOM manipulation\n"
            "• Async/await and promises\n"
            "• ES6+ features\n\n"
            "**Frameworks:**\n"
            "• React, Vue, Angular (Frontend)\n"
            "• Node.js, Express (Backend)\n"
            "• Next.js (Full-stack)\n"
        )
    
    def _explain_algorithm(self):
        """Explain algorithms"""
        return (
            "🧮 **Algorithms**\n\n"
            "An algorithm is a step-by-step procedure to solve a problem.\n\n"
            "**Types:**\n"
            "• Sorting (Bubble, Quick, Merge)\n"
            "• Searching (Binary, Linear)\n"
            "• Graph algorithms (BFS, DFS, Dijkstra)\n"
            "• Dynamic Programming\n"
            "• Greedy algorithms\n\n"
            "**Complexity Analysis:**\n"
            "• Time Complexity: How long it takes\n"
            "• Space Complexity: How much memory it uses\n"
            "• Big O notation: O(n), O(log n), O(n²)\n\n"
            "**Practice Platforms:**\n"
            "• LeetCode\n"
            "• HackerRank\n"
            "• CodeChef\n"
            "• GeeksforGeeks"
        )
    
    def _explain_data_structure(self):
        """Explain data structures"""
        return (
            "📚 **Data Structures**\n\n"
            "Data structures are ways to organize and store data.\n\n"
            "**Types:**\n\n"
            "**Linear:**\n"
            "• Array: Fixed-size, indexed collection\n"
            "• Linked List: Dynamic, node-based\n"
            "• Stack: LIFO (Last In First Out)\n"
            "• Queue: FIFO (First In First Out)\n\n"
            "**Non-Linear:**\n"
            "• Tree: Hierarchical structure\n"
            "• Graph: Nodes and edges\n"
            "• Hash Table: Key-value pairs\n\n"
            "**When to Use:**\n"
            "• Arrays: Random access needed\n"
            "• Linked Lists: Dynamic size, frequent insertions\n"
            "• Stacks: Undo operations, recursion\n"
            "• Queues: Task scheduling\n"
            "• Trees: Hierarchical data (file systems)\n"
            "• Graphs: Social networks, maps"
        )
    
    def _get_default_response(self, query):
        """Default intelligent response for unmatched queries"""
        responses = [
            f"I understand you're asking about '{query}'. Let me help you with that!\n\n"
            "I can assist you with:\n"
            "• Study planning and exam preparation\n"
            "• Explaining technical concepts (DBMS, Programming, etc.)\n"
            "• Hackathon and project ideas\n"
            "• Assignment help\n"
            "• Placement and career guidance\n"
            "• Attendance tracking\n\n"
            "Could you rephrase your question or ask about one of these topics?",
            
            f"That's an interesting question! While I'm analyzing your query about '{query}',\n\n"
            "Here's what I can help you with:\n"
            "📚 Study plans and exam strategies\n"
            "💡 Technical concept explanations\n"
            "🚀 Project and hackathon ideas\n"
            "📝 Assignment guidance\n"
            "🎯 Career and placement tips\n\n"
            "Feel free to ask me anything related to your college journey!",
        ]
        return random.choice(responses)

