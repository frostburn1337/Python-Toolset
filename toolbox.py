import tkinter as tk
import subprocess
from splash import show_splash_screen

def launch_application_1():
    subprocess.run(["python", "to-do.py"])

def launch_application_2():
    print("Launching Application 2...")

def launch_application_3():
    print("Launching Application 3...")

def main(): 
    show_splash_screen(message="Welcome to the toolbox application", font_size=32)
    
    root = tk.Tk()
    root.title("Toolbox Menu")

    width = 640
    height = 480
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    x_coordinate = (screen_width - width) // 2
    y_coordinate = (screen_height - height) // 2
    root.geometry(f"{width}x{height}+{x_coordinate}+{y_coordinate}")

    button1 = tk.Button(root, text="Launch To-Do List", command=launch_application_1)
    button1.pack(pady=5)
    button2 = tk.Button(root, text="Launch Application 2", command=launch_application_2)
    button2.pack(pady=5)
    button3 = tk.Button(root, text="Launch Application 3", command=launch_application_3)
    button3.pack(pady=5)

    quit_button = tk.Button(root, text="Exit", command=root.quit)
    quit_button.pack(pady=5)

    root.mainloop()

if __name__ == "__main__":
    main()