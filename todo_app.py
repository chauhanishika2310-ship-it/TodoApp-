import tkinter as tk
from tkinter import messagebox
import os

class ToDoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List App")
        self.root.geometry("400x400")
        self.tasks = []

        self.task_entry = tk.Entry(root, font=("Arial", 14))
        self.task_entry.pack(pady=10)

        self.add_button = tk.Button(root, text="Add Task", command=self.add_task)
        self.add_button.pack()

        self.task_listbox = tk.Listbox(root, font=("Arial", 12), width=40, height=10)
        self.task_listbox.pack(pady=10)

        self.delete_button = tk.Button(root, text="Delete Selected", command=self.delete_task)
        self.delete_button.pack()

        self.save_button = tk.Button(root, text="Save Tasks", command=self.save_tasks)
        self.save_button.pack()

        self.load_button = tk.Button(root, text="Load Tasks", command=self.load_tasks)
        self.load_button.pack()

    def add_task(self):
        task = self.task_entry.get()
        if task != "":
            self.task_listbox.insert(tk.END, task)
            self.task_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Input Error", "Please enter a task.")

    def delete_task(self):
        try:
            index = self.task_listbox.curselection()
            self.task_listbox.delete(index)
        except:
            messagebox.showwarning("Delete Error", "Please select a task to delete.")

    def save_tasks(self):
        tasks = self.task_listbox.get(0, tk.END)
        with open("tasks.txt", "w") as file:
            for task in tasks:
                file.write(task + "\n")
        messagebox.showinfo("Saved", "Tasks saved to tasks.txt")

    def load_tasks(self):
        if not os.path.exists("tasks.txt"):
            messagebox.showwarning("No File", "tasks.txt not found.")
            return
        self.task_listbox.delete(0, tk.END)
        with open("tasks.txt", "r") as file:
            for task in file:
                self.task_listbox.insert(tk.END, task.strip())

if __name__ == "__main__":
    root = tk.Tk()
    app = ToDoApp(root)
    root.mainloop()
