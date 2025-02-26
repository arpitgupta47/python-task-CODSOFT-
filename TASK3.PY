import os
import json
from datetime import datetime

class ToDoList:
    def __init__(self):
        self.tasks = []
        self.filename = "todo_data.json"
        self.load_tasks()

    def load_tasks(self):
        """Load tasks from the JSON file if it exists."""
        if os.path.exists(self.filename):
            try:
                with open(self.filename, 'r') as file:
                    self.tasks = json.load(file)
            except json.JSONDecodeError:
                print("Error loading tasks. Starting with an empty list.")
                self.tasks = []
        else:
            self.tasks = []

    def save_tasks(self):
        """Save tasks to the JSON file."""
        with open(self.filename, 'w') as file:
            json.dump(self.tasks, file, indent=4)

    def add_task(self, title, description="", due_date=None, priority="medium"):
        """Add a new task to the list."""
        task = {
            "id": len(self.tasks) + 1,
            "title": title,
            "description": description,
            "due_date": due_date,
            "priority": priority,
            "status": "pending",
            "created_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }
        self.tasks.append(task)
        self.save_tasks()
        print(f"Task added: {title}")

    def view_tasks(self, filter_status=None):
        """Display all tasks or filter by status."""
        if not self.tasks:
            print("No tasks found.")
            return

        filtered_tasks = self.tasks
        if filter_status:
            filtered_tasks = [task for task in self.tasks if task["status"] == filter_status]
            if not filtered_tasks:
                print(f"No tasks with status '{filter_status}' found.")
                return

        print("\n" + "="*80)
        print(f"{'ID':<5}{'Title':<30}{'Due Date':<15}{'Priority':<10}{'Status':<10}")
        print("-"*80)
        
        for task in filtered_tasks:
            print(f"{task['id']:<5}{task['title'][:28]:<30}{task.get('due_date', 'None'):<15}{task['priority']:<10}{task['status']:<10}")
        
        print("="*80 + "\n")

    def view_task_details(self, task_id):
        """Display detailed information about a specific task."""
        task = self.get_task_by_id(task_id)
        if task:
            print("\n" + "="*80)
            print(f"Task ID: {task['id']}")
            print(f"Title: {task['title']}")
            print(f"Description: {task['description']}")
            print(f"Due Date: {task.get('due_date', 'None')}")
            print(f"Priority: {task['priority']}")
            print(f"Status: {task['status']}")
            print(f"Created: {task['created_at']}")
            print("="*80 + "\n")
        else:
            print(f"Task with ID {task_id} not found.")

    def get_task_by_id(self, task_id):
        """Helper function to get a task by its ID."""
        for task in self.tasks:
            if task["id"] == task_id:
                return task
        return None

    def update_task(self, task_id, field, value):
        """Update a specific field of a task."""
        task = self.get_task_by_id(task_id)
        if task:
            if field in task:
                task[field] = value
                self.save_tasks()
                print(f"Task {task_id} updated: {field} = {value}")
            else:
                print(f"Field '{field}' does not exist.")
        else:
            print(f"Task with ID {task_id} not found.")

    def delete_task(self, task_id):
        """Delete a task by its ID."""
        task = self.get_task_by_id(task_id)
        if task:
            self.tasks.remove(task)
            
            for i, task in enumerate(self.tasks, 1):
                task["id"] = i
            self.save_tasks()
            print(f"Task {task_id} deleted.")
        else:
            print(f"Task with ID {task_id} not found.")

    def mark_complete(self, task_id):
        """Mark a task as complete."""
        self.update_task(task_id, "status", "completed")

    def mark_pending(self, task_id):
        """Mark a task as pending."""
        self.update_task(task_id, "status", "pending")

def display_menu():
    """Display the application menu."""
    print("\n==== To-Do List Menu ====")
    print("1. Add new task")
    print("2. View all tasks")
    print("3. View task details")
    print("4. Update task")
    print("5. Delete task")
    print("6. Mark task as complete")
    print("7. View completed tasks")
    print("8. View pending tasks")
    print("9. Exit")
    return input("Enter your choice (1-9): ")

def main():
    todo_list = ToDoList()
    print("Welcome to the To-Do List Application!")
    
    while True:
        choice = display_menu()
        
        if choice == '1':
            title = input("Enter task title: ")
            description = input("Enter task description (optional): ")
            due_date = input("Enter due date (YYYY-MM-DD) (optional): ")
            if due_date == "":
                due_date = None
            priority = input("Enter priority (low/medium/high) (default: medium): ").lower()
            if priority not in ["low", "medium", "high"]:
                priority = "medium"
            todo_list.add_task(title, description, due_date, priority)
            
        elif choice == '2':
            todo_list.view_tasks()
            
        elif choice == '3':
            try:
                task_id = int(input("Enter task ID: "))
                todo_list.view_task_details(task_id)
            except ValueError:
                print("Please enter a valid task ID (number).")
            
        elif choice == '4':
            try:
                task_id = int(input("Enter task ID to update: "))
                print("Fields: title, description, due_date, priority")
                field = input("Enter field to update: ").lower()
                if field in ["title", "description", "due_date", "priority"]:
                    value = input(f"Enter new value for {field}: ")
                    todo_list.update_task(task_id, field, value)
                else:
                    print("Invalid field name.")
            except ValueError:
                print("Please enter a valid task ID (number).")
            
        elif choice == '5':
            try:
                task_id = int(input("Enter task ID to delete: "))
                confirm = input(f"Are you sure you want to delete task {task_id}? (y/n): ").lower()
                if confirm == 'y':
                    todo_list.delete_task(task_id)
            except ValueError:
                print("Please enter a valid task ID (number).")
            
        elif choice == '6':
            try:
                task_id = int(input("Enter task ID to mark as complete: "))
                todo_list.mark_complete(task_id)
            except ValueError:
                print("Please enter a valid task ID (number).")
            
        elif choice == '7':
            todo_list.view_tasks("completed")
            
        elif choice == '8':
            todo_list.view_tasks("pending")
            
        elif choice == '9':
            print("Thank you for using the To-Do List Application!")
            break
            
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()