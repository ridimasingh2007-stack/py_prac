import tkinter as tk
from tkinter import messagebox


root = tk.Tk()
root.title("Simple To-Do List")


def add_task():
    task = task_entry.get()
    if task != "":
        task_listbox.insert(tk.END, task)
        task_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "You must enter a task!")


def delete_task():
    try:
        selected_task_index = task_listbox.curselection()[0]
        task_listbox.delete(selected_task_index)
    except IndexError:
        messagebox.showwarning("Warning", "Please select a task to delete.")


task_entry = tk.Entry(root, width=40)
task_entry.pack(pady=10)


add_button = tk.Button(root, text="Add Task", width=20, command=add_task)
add_button.pack(pady=5)


task_listbox = tk.Listbox(root, width=50, height=10)
task_listbox.pack(pady=10)


delete_button = tk.Button(root, text="Delete Selected Task", width=20, command=delete_task)
delete_button.pack(pady=5)


root.mainloop()
