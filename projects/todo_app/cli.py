# cli.py

from todo_manager import TodoManager

def main():
    manager = TodoManager()

    while True:
        print("\n📌 To-Do List Manager")
        print("1. Add Task")
        print("2. List Tasks")
        print("3. Toggle Task Completion")
        print("4. Remove Task")
        print("5. Exit")
        
        choice = input("Enter your choice: ")

        if choice == "1":
            title = input("Enter task title: ")
            description = input("Enter task description: ")
            task = manager.add_task(title, description)
            print(f"✅ Task '{task.title}' added.")

        elif choice == "2":
            tasks = manager.list_tasks()
            if not tasks:
                print("No tasks found.")
            for task in tasks:
                print(task)

        elif choice == "3":
            task_id = input("Enter Task ID to toggle: ")
            task = manager.toggle_task(task_id)
            if task:
                print(f"🔄 Task '{task.title}' updated.")
            else:
                print("⚠️ Task not found.")

        elif choice == "4":
            task_id = input("Enter Task ID to remove: ")
            manager.remove_task(task_id)
            print("🗑️ Task removed.")

        elif choice == "5":
            print("👋 Goodbye!")
            break
        
        else:
            print("⚠️ Invalid choice, try again.")

if __name__ == "__main__":
    main()
