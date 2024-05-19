import tkinter as tk
from tkinter import messagebox

class ToDoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List App")

        self.tasks = []

        self.frame = tk.Frame(self.root)
        self.frame.pack(pady=10)

        self.task_entry = tk.Entry(self.frame, width=30)
        self.task_entry.grid(row=0, column=0, padx=5)
        
        self.add_task_btn = tk.Button(self.frame, text="Add Task", command=self.add_task)
        self.add_task_btn.grid(row=0, column=1)

        self.task_listbox = tk.Listbox(self.root, width=50, height=15)
        self.task_listbox.pack(pady=10)

        self.delete_task_btn = tk.Button(self.root, text="Delete Task", command=self.delete_task)
        self.delete_task_btn.pack(pady=5)
        
        self.mark_completed_btn = tk.Button(self.root, text="Mark as Completed", command=self.mark_completed)
        self.mark_completed_btn.pack(pady=5)

    def add_task(self):
        task = self.task_entry.get()
        if task != "":
            self.tasks.append(task)
            self.update_task_listbox()
            self.task_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Warning", "You must enter a task.")

    def delete_task(self):
        try:
            selected_task_index = self.task_listbox.curselection()[0]
            del self.tasks[selected_task_index]
            self.update_task_listbox()
        except IndexError:
            messagebox.showwarning("Warning", "You must select a task to delete.")

    def mark_completed(self):
        try:
            selected_task_index = self.task_listbox.curselection()[0]
            task = self.tasks[selected_task_index]
            self.tasks[selected_task_index] = task + " ✔"
            self.update_task_listbox()
        except IndexError:
            messagebox.showwarning("Warning", "You must select a task to mark as completed.")

    def update_task_listbox(self):
        self.task_listbox.delete(0, tk.END)
        for task in self.tasks:
            self.task_listbox.insert(tk.END, task)

if __name__ == "__main__":
    root = tk.Tk()
    app = ToDoApp(root)
    root.mainloop()
