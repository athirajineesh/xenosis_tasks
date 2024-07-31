import tkinter as tk
from tkinter import messagebox
import os

# File where tasks will be saved
FILE = "tasks.txt"

class TodoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List Application")

        # Create GUI components
        self.create_widgets()

        # Load tasks from file
        self.load_tasks()

    def create_widgets(self):
        # Listbox to display tasks
        self.task_listbox = tk.Listbox(self.root, selectmode=tk.SINGLE, width=70, height=20, bg='LemonChiffon', activestyle="none")
        self.task_listbox.pack(pady=10)

        # Entry widget to input new tasks
        self.task_entry = tk.Entry(self.root, width=70)
        self.task_entry.pack(pady=5)

        # Buttons to add, delete and mark tasks
        self.add_button = tk.Button(self.root, text="Add Task",  command=self.add_task, bg='green', fg='black')
        self.add_button.pack(pady=5)

        self.delete_button = tk.Button(self.root, text="Delete Task", command=self.delete_task, bg='red', fg='black')
        self.delete_button.pack(pady=5)

        self.mark_button = tk.Button(self.root, text="Mark Complete", command=self.mark_complete, bg='violet', fg='black')
        self.mark_button.pack(pady=5)

    def add_task(self):
        task = self.task_entry.get()
        if task:
            self.task_listbox.insert(tk.END, task)
            self.task_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Warning", "You must enter a task.")

    def delete_task(self):
        selected_task_index = self.task_listbox.curselection()
        if selected_task_index:
            self.task_listbox.delete(selected_task_index)
        else:
            messagebox.showwarning("Warning", "You must select a task to delete.")

    def mark_complete(self):
        selected_task_index = self.task_listbox.curselection()
        if selected_task_index:
            task = self.task_listbox.get(selected_task_index)
            if not task.endswith("[Completed]"):
                self.task_listbox.delete(selected_task_index)
                self.task_listbox.insert(selected_task_index, f" {task} [Completed]")

        else:
            messagebox.showwarning("Warning", "You must select a task to mark as complete.")

    def save_tasks(self):
        with open(FILE, 'w') as file:
            for task in self.task_listbox.get(0, tk.END):
                file.write(task + '\n')

    def load_tasks(self):
        if os.path.exists(FILE):
            with open(FILE, 'r') as file:
                for line in file:
                    self.task_listbox.insert(tk.END, line.strip())

    def on_closing(self):
        self.save_tasks()
        self.root.destroy()

def main():
    root = tk.Tk()
    app = TodoApp(root)
    root.protocol("WM_DELETE_WINDOW", app.on_closing)
    root.mainloop()


main()
