import tkinter as tk
from tkinter import messagebox

class ToDoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List Application")
        self.root.geometry("400x500")
        
        # List to store tasks
        self.tasks = []

        # Title label
        self.title_label = tk.Label(root, text="To-Do List", font=("Arial", 18, "bold"))
        self.title_label.pack(pady=10)

        # Task display
        self.task_frame = tk.Frame(root)
        self.task_frame.pack(pady=10, fill=tk.BOTH, expand=True)
        
        self.task_listbox = tk.Listbox(self.task_frame, font=("Arial", 14))
        self.task_listbox.pack(fill=tk.BOTH, expand=True, padx=10, pady=5)

        # Task input
        self.task_entry = tk.Entry(root, font=("Arial", 14), width=30)
        self.task_entry.pack(pady=10)

        # Buttons
        self.add_button = tk.Button(root, text="Add Task", font=("Arial", 12), command=self.add_task)
        self.add_button.pack(pady=5)
        
        self.update_button = tk.Button(root, text="Update Task", font=("Arial", 12), command=self.update_task)
        self.update_button.pack(pady=5)
        
        self.delete_button = tk.Button(root, text="Delete Task", font=("Arial", 12), command=self.delete_task)
        self.delete_button.pack(pady=5)

        self.clear_button = tk.Button(root, text="Clear All Tasks", font=("Arial", 12), command=self.clear_tasks)
        self.clear_button.pack(pady=5)

    def add_task(self):
        task = self.task_entry.get()
        if task:
            self.tasks.append(task)
            self.task_listbox.insert(tk.END, task)
            self.task_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Input Error", "Please enter a task!")

    def update_task(self):
        selected_index = self.task_listbox.curselection()
        if selected_index:
            new_task = self.task_entry.get()
            if new_task:
                index = selected_index[0]
                self.tasks[index] = new_task
                self.task_listbox.delete(index)
                self.task_listbox.insert(index, new_task)
                self.task_entry.delete(0, tk.END)
            else:
                messagebox.showwarning("Input Error", "Please enter a new task to update!")
        else:
            messagebox.showwarning("Selection Error", "Please select a task to update!")

    def delete_task(self):
        selected_index = self.task_listbox.curselection()
        if selected_index:
            index = selected_index[0]
            self.tasks.pop(index)
            self.task_listbox.delete(index)
        else:
            messagebox.showwarning("Selection Error", "Please select a task to delete!")

    def clear_tasks(self):
        if messagebox.askyesno("Clear All", "Are you sure you want to clear all tasks?"):
            self.tasks.clear()
            self.task_listbox.delete(0, tk.END)

if __name__ == "__main__":
    root = tk.Tk()
    app = ToDoApp(root)
    root.mainloop()

