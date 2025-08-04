"""
Simple Todo List Application
A basic todo list manager for demonstrating Claude Code's code generation capabilities
"""

import json
import os
from datetime import datetime

class TodoApp:
    def __init__(self, filename='todos.json'):
        self.filename = filename
        self.todos = self.load_todos()
    
    def load_todos(self):
        """Load todos from file"""
        if os.path.exists(self.filename):
            with open(self.filename, 'r') as f:
                return json.load(f)
        return []
    
    def save_todos(self):
        """Save todos to file"""
        with open(self.filename, 'w') as f:
            json.dump(self.todos, f, indent=2)
    
    def add_todo(self, task):
        """Add a new todo item"""
        todo = {
            'id': len(self.todos) + 1,
            'task': task,
            'completed': False,
            'created_at': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        }
        self.todos.append(todo)
        self.save_todos()
        return todo
    
    def list_todos(self, show_completed=True):
        """List all todos"""
        if not show_completed:
            return [t for t in self.todos if not t['completed']]
        return self.todos
    
    def complete_todo(self, todo_id):
        """Mark a todo as completed"""
        for todo in self.todos:
            if todo['id'] == todo_id:
                todo['completed'] = True
                todo['completed_at'] = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                self.save_todos()
                return True
        return False
    
    def delete_todo(self, todo_id):
        """Delete a todo"""
        self.todos = [t for t in self.todos if t['id'] != todo_id]
        self.save_todos()

def main():
    app = TodoApp()
    
    while True:
        print("\n--- Todo List Manager ---")
        print("1. Add todo")
        print("2. List todos")
        print("3. Complete todo")
        print("4. Delete todo")
        print("5. Exit")
        
        choice = input("\nChoose an option: ")
        
        if choice == '1':
            task = input("Enter task: ")
            todo = app.add_todo(task)
            print(f"Added: {todo['task']} (ID: {todo['id']})")
        
        elif choice == '2':
            todos = app.list_todos()
            if not todos:
                print("No todos found!")
            else:
                for todo in todos:
                    status = "✓" if todo['completed'] else "○"
                    print(f"{status} [{todo['id']}] {todo['task']}")
        
        elif choice == '3':
            todo_id = int(input("Enter todo ID to complete: "))
            if app.complete_todo(todo_id):
                print("Todo completed!")
            else:
                print("Todo not found!")
        
        elif choice == '4':
            todo_id = int(input("Enter todo ID to delete: "))
            app.delete_todo(todo_id)
            print("Todo deleted!")
        
        elif choice == '5':
            print("Goodbye!")
            break

if __name__ == "__main__":
    main()