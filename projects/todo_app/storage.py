# storage.py

import json
import os
from models import Task

class Storage:
    """Handles saving and loading tasks from a JSON file."""
    
    def __init__(self, filename="tasks.json"):
        self.filename = filename

    def save_tasks(self, tasks):
        """Save tasks to a JSON file."""
        with open(self.filename, "w") as f:
            json.dump([task.__dict__ for task in tasks], f, indent=4)

    def load_tasks(self):
        """Load tasks from a JSON file."""
        if not os.path.exists(self.filename):
            return []
        with open(self.filename, "r") as f:
            data = json.load(f)
            return [Task(**task) for task in data]
