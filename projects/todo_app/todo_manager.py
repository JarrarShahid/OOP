# todo_manager.py

import json
import os
from models import Task

class TodoManager:
    """Manages the to-do list tasks (CRUD operations)."""

    def __init__(self, storage_file="tasks.json"):
        self.storage_file = storage_file
        self.tasks = self.load_tasks()

    def add_task(self, title, description=""):
        """Add a new task."""
        task = Task(title, description)
        self.tasks.append(task)
        self.save_tasks()
        return task

    def remove_task(self, task_id):
        """Remove a task by ID."""
        self.tasks = [task for task in self.tasks if task.id != task_id]
        self.save_tasks()

    def list_tasks(self):
        """List all tasks."""
        return self.tasks

    def toggle_task(self, task_id):
        """Toggle task completion status."""
        for task in self.tasks:
            if task.id == task_id:
                task.mark_complete() if not task.completed else task.mark_incomplete()
                self.save_tasks()
                return task
        return None

    def save_tasks(self):
        """Save tasks to a JSON file."""
        with open(self.storage_file, "w") as f:
            json.dump([task.__dict__ for task in self.tasks], f, indent=4)

    def load_tasks(self):
        """Load tasks from a JSON file."""
        if not os.path.exists(self.storage_file):
            return []
        with open(self.storage_file, "r") as f:
            data = json.load(f)
            return [Task(**task) for task in data]
