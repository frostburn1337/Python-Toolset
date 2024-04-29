import tkinter as tk
from datetime import datetime

def show_splash_screen(title="Welcome", message="Good morning, Victoria!", font_size=48, width=800, height=600, duration=3000):
    current_time = datetime.now().strftime("%H:%M")
    message_with_time = f"{message}\n\nThe time is {current_time}"
    
    splash_root = tk.Tk()
    splash_root.title(title)

    screen_width = splash_root.winfo_screenwidth()
    screen_height = splash_root.winfo_screenheight()
    x_coordinate = (screen_width - width) // 2
    y_coordinate = (screen_height - height) // 2
    splash_root.geometry(f"{width}x{height}+{x_coordinate}+{y_coordinate}")

    font_style = ("Arial", font_size)
    splash_label = tk.Label(splash_root, text=message_with_time, font=font_style)
    splash_label.pack(expand=True, fill=tk.BOTH)
    splash_root.after(duration, splash_root.destroy)
    splash_root.mainloop()

def main():
    show_splash_screen()

if __name__ == "__main__":
    main()