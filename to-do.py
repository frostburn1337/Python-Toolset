import tkinter as tk
from splash import show_splash_screen

def add_task():
    task = entry.get()
    if task:
        listbox.insert(tk.END, task)
        entry.delete(0, tk.END)

def delete_task():
    selected = listbox.curselection()
    if selected:
        listbox.delete(selected)

def mark_completed():
    selected = listbox.curselection()
    if selected:
        listbox.itemconfig(selected, {'bg': 'light grey'})

def main(): 
    show_splash_screen(message="Welcome to the to-do list application", font_size=32)

    root = tk.Tk()
    root.title("To-Do List")

    width = 480
    height = 480
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    x_coordinate = (screen_width - width) // 2
    y_coordinate = (screen_height - height) // 2
    root.geometry(f"{width}x{height}+{x_coordinate}+{y_coordinate}")

    global entry
    entry = tk.Entry(root, width=50)
    entry.pack(pady=10)

    global listbox
    listbox = tk.Listbox(root, width=50)
    listbox.pack()

    add_button = tk.Button(root, text="Add Task", command=add_task)
    add_button.pack(pady=5)
    delete_button = tk.Button(root, text="Delete Task", command=delete_task)
    delete_button.pack(pady=5)
    mark_button = tk.Button(root, text="Mark Completed", command=mark_completed)
    mark_button.pack(pady=5)

    root.mainloop()

if __name__ == "__main__":
    main()