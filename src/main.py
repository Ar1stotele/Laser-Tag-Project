from tktest import *

main_gui = GUI()

main_gui.show_splash_screen()
root.after(3000, main_gui.main_window)


tk.mainloop()