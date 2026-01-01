"""
Script to reset the database
Run: python reset_db.py
"""
import os
import sys

# Add project to path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

# Change to project directory
os.chdir(os.path.join(os.path.dirname(__file__), 'randomproject'))

# Delete database if exists
db_path = 'db.sqlite3'
if os.path.exists(db_path):
    try:
        os.remove(db_path)
        print(f"✅ Deleted {db_path}")
    except Exception as e:
        print(f"❌ Could not delete {db_path}: {e}")
        print("Please close any running Django servers and try again.")
        sys.exit(1)
else:
    print(f"ℹ️  {db_path} does not exist")

print("\n✅ Database reset complete!")
print("Now run: python manage.py migrate")

