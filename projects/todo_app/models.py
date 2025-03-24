# models.py

import uuid
from datetime import datetime

class Task:
    """Represents a single task in the to-do list."""
    
    def __init__(self, title, description="", completed=False):
        self.id = str(uuid.uuid4())  # Unique identifier for each task
        self.title = title
        self.description = description
        self.completed = completed
        self.created_at = datetime.now()

    def mark_complete(self):
        """Mark the task as completed."""
        self.completed = True

    def mark_incomplete(self):
        """Mark the task as incomplete."""
        self.completed = False

    def __str__(self):
        """String representation of a task."""
        status = "✅" if self.completed else "❌"
        return f"[{status}] {self.title} - {self.description} (Created: {self.created_at.strftime('%Y-%m-%d %H:%M')})"
