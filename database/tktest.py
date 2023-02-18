
import database
import tkinter as tk
from tkinter import *
from PIL import ImageTk, Image


##TkInter's instance 
root = tk.Tk()

class playerEntry:

	

	def __init__(self, container):
	
		self.PlayerID = None
		self.Codename = None
		
		self.L1 = Label(container, text="Player ID:")
		self.L1.pack(side = "left")
		
		self.B2 = Button(container, text = ">", command = self.newCodename)
		self.B2.pack(side = "right")
		
		self.E2 = Entry(container)
		self.E2.pack(side = "right")
		
		self.L2 = Label(container, text="Codename:")
		self.L2.pack(side = "right")
		
		self.E1 = Entry(container)
		self.E1.pack(side = "left")
		
		self.B1 = Button(container, text = ">", command = self.getPlayer)
		self.B1.pack(side = "left")
		
		
		
	
	def getPlayer(self):
	
		self.PlayerID = self.E1.get()
		
		#Disable the playerID entry box
		self.E1.config(state = "disabled")
		self.B1.config(state = "disabled")
		
		#If player already exists in database, get the codename
		if(database.getPlayerID(self.PlayerID)):
			
			#Disable the entry and button, add the codename into the entry
			self.Codename = database.getCodename(self.PlayerID)
			
			
			self.E2.insert(0, self.Codename)
			
			self.E2.config(state = "disabled")
			self.B2.config(state = "disabled")

	def newCodename(self):
		print("hello")
		
		
	

def show_splash_screen():
	global splash_screen_image
	# define title of the application
	root.title("test")
	# define size of the window -> in the future add autoamatic adjustment to the user resolution
	root.geometry("800x700+400-100")
		
	# to hide menu during splash screen
	root.overrideredirect(True)

def main_window():
    # destroying splash screen
	root.destroy()

    # creating main screen
	main_root = tk.Tk()
	main_root.title("test application")
	main_root.geometry("800x700+400-100")
	
	
	team1_container=Frame(main_root, relief="sunken", borderwidth=2)
	team1_container.pack(side="left", fill="x")
	
	team2_container=Frame(main_root, relief="sunken", borderwidth=2)
	team2_container.pack(side="left", fill="x")
	
	p1 = playerEntry(team1_container)
	p2 = playerEntry(team2_container)
	


	

	


show_splash_screen()
root.after(300, main_window)


tk.mainloop()