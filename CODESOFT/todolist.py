import tkinter as tk
from tkinter import messagebox, simpledialog

class TodoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List Application")
        
        self.tasks = []
        
        # Set up GUI components
        self.setup_ui()
        
    def setup_ui(self):
        # Frame for the task entry
        entry_frame = tk.Frame(self.root)
        entry_frame.pack(pady=10)
        
        self.task_entry = tk.Entry(entry_frame, width=40)
        self.task_entry.pack(side=tk.LEFT, padx=10)
        
        add_button = tk.Button(entry_frame, text="Add Task", command=self.add_task)
        add_button.pack(side=tk.LEFT)
        
        # Frame for the task list
        list_frame = tk.Frame(self.root)
        list_frame.pack(pady=10)
        
        self.task_listbox = tk.Listbox(list_frame, width=50, height=10, selectmode=tk.SINGLE)
        self.task_listbox.pack(side=tk.LEFT, padx=10)
        
        scrollbar = tk.Scrollbar(list_frame, orient=tk.VERTICAL, command=self.task_listbox.yview)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        
        self.task_listbox.config(yscrollcommand=scrollbar.set)
        
        # Frame for action buttons
        action_frame = tk.Frame(self.root)
        action_frame.pack(pady=10)
        
        delete_button = tk.Button(action_frame, text="Delete Task", command=self.delete_task)
        delete_button.pack(side=tk.LEFT, padx=5)
        
        complete_button = tk.Button(action_frame, text="Mark as Completed", command=self.complete_task)
        complete_button.pack(side=tk.LEFT, padx=5)
        
        save_button = tk.Button(action_frame, text="Save Tasks", command=self.save_tasks)
        save_button.pack(side=tk.LEFT, padx=5)
        
        load_button = tk.Button(action_frame, text="Load Tasks", command=self.load_tasks)
        load_button.pack(side=tk.LEFT, padx=5)
        
    def add_task(self):
        task = self.task_entry.get().strip()
        if task:
            self.tasks.append(task)
            self.update_task_list()
            self.task_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Warning", "You must enter a task.")
    
    def delete_task(self):
        try:
            selected_index = self.task_listbox.curselection()[0]
            self.tasks.pop(selected_index)
            self.update_task_list()
        except IndexError:
            messagebox.showwarning("Warning", "You must select a task to delete.")
    
    def complete_task(self):
        try:
            selected_index = self.task_listbox.curselection()[0]
            self.tasks[selected_index] = f"{self.tasks[selected_index]} (Completed)"
            self.update_task_list()
        except IndexError:
            messagebox.showwarning("Warning", "You must select a task to mark as completed.")
    
    def update_task_list(self):
        self.task_listbox.delete(0, tk.END)
        for task in self.tasks:
            self.task_listbox.insert(tk.END, task)
    
    def save_tasks(self):
        with open("tasks.txt", "w") as file:
            for task in self.tasks:
                file.write(task + "\n")
        messagebox.showinfo("Info", "Tasks saved successfully.")
    
    def load_tasks(self):
        try:
            with open("tasks.txt", "r") as file:
                self.tasks = [line.strip() for line in file.readlines()]
            self.update_task_list()
        except FileNotFoundError:
            messagebox.showwarning("Warning", "No saved tasks found.")

# Set up the main application window
if __name__ == "__main__":
    root = tk.Tk()
    app = TodoApp(root)
    root.mainloop()
