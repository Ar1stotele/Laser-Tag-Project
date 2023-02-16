import tkinter as tk
from PIL import ImageTk, Image
import constants as config

# TkInter's instance 
root = tk.Tk()

# splash screen function 
def show_splash_screen():
    global splash_screen_image
    # define title of the application
    root.title(config.application_title)
    # define size of the window -> in the future add autoamatic adjustment to the user resolution
    root.geometry("800x700+400-100")
    
    # to hide menu during splash screen
    root.overrideredirect(True)

    # splash screen image 
    splash_screen_image_open = Image.open("../assets/logo.jpg")
    splash_screen_image_resized = splash_screen_image_open.resize((800,700), Image.LANCZOS)
    splash_screen_image = ImageTk.PhotoImage(splash_screen_image_resized)

    my_label = tk.Label(image=splash_screen_image)
    my_label.grid(column=0, row=0)


def main_window():
    # destroying splash screen
    root.destroy()

    # creating main screen
    main_root = tk.Tk()
    main_root.title(config.application_title)
    main_root.geometry("800x700+400-100")

    my_label = tk.Label(main_root, text="main hello window")
    my_label.grid(row=0, column=0)        

