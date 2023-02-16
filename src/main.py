import tkinter as tk
import gui

gui.show_splash_screen()
gui.root.after(3000, gui.main_window)

tk.mainloop()
