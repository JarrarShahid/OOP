# gui_app.py

import tkinter as tk
from tkinter import messagebox

class TaskManager:
    """Manages the task list"""
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        """Adds a task to the list"""
        if task and task not in self.tasks:
            self.tasks.append(task)
            return True
        return False

    def remove_task(self, task):
        """Removes a task from the list"""
        if task in self.tasks:
            self.tasks.remove(task)
            return True
        return False

    def get_tasks(self):
        """Returns the list of tasks"""
        return self.tasks


class TodoApp:
    """GUI Application for the To-Do List"""
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List App")
        self.root.geometry("400x500")

        self.task_manager = TaskManager()

        # UI Components
        self.task_entry = tk.Entry(root, width=40)
        self.task_entry.pack(pady=10)

        self.add_button = tk.Button(root, text="Add Task", command=self.add_task)
        self.add_button.pack()

        self.task_listbox = tk.Listbox(root, width=50, height=15)
        self.task_listbox.pack(pady=10)

        self.remove_button = tk.Button(root, text="Remove Task", command=self.remove_task)
        self.remove_button.pack()

    def add_task(self):
        """Adds a task to the list"""
        task = self.task_entry.get()
        if self.task_manager.add_task(task):
            self.task_listbox.insert(tk.END, task)
            self.task_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Warning", "Task cannot be empty or duplicate!")

    def remove_task(self):
        """Removes the selected task"""
        try:
            selected_task = self.task_listbox.get(tk.ACTIVE)
            if self.task_manager.remove_task(selected_task):
                self.task_listbox.delete(tk.ACTIVE)
        except:
            messagebox.showwarning("Warning", "No task selected!")

# Run the application
if __name__ == "__main__":
    root = tk.Tk()
    app = TodoApp(root)
    root.mainloop()
