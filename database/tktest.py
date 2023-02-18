
import database
import tkinter as tk
from tkinter import *
from PIL import ImageTk, Image


##TkInter's instance 
root = tk.Tk()


#Creates a single player entry box 
class playerEntry:

	def __init__(self, container):
	
		self.PlayerID = None
		self.Codename = None
		
		self.frame = Frame(container, relief="sunken", borderwidth=2)
		self.frame.pack(side = "top")
		
		self.L1 = Label(self.frame, text="Player ID:")
		self.L1.pack(side = "left")
		
		self.E1 = Entry(self.frame)
		self.E1.pack(side = "left")
		
		self.B1 = Button(self.frame, text = ">", command = self.getPlayer)
		self.B1.pack(side = "left")
		
		self.B2 = Button(self.frame, text = ">", command = self.newCodename, state = "disabled")
		self.B2.pack(side = "right")
		
		self.E2 = Entry(self.frame)
		self.E2.pack(side = "right")
		
		self.L2 = Label(self.frame, text="Codename:")
		self.L2.pack(side = "right")
		
		
	
	def getPlayer(self):
	
		self.PlayerID = self.E1.get()
		
		#Disable the playerID entry box
		self.E1.config(state = "disabled")
		self.B1.config(state = "disabled")
		
		self.B2.config(state = "active")
		
		#If player already exists in database, get the codename
		#If the player does not exist, player ID is added to the database 
		if(database.getPlayerID(self.PlayerID)):
			
			#Disable the entry and button, add the codename into the entry
			self.Codename = database.getCodename(self.PlayerID)
			
			#Disable entering a codename, as this is fetched from database
			self.E2.insert(0, self.Codename)
			
			self.E2.config(state = "disabled")
			self.B2.config(state = "disabled")

	def newCodename(self):
		self.Codename = self.E2.get()
		self.E2.config(state = "disabled")
		#Update the codename of the corresponding id in the database
		database.insertCodename(self.PlayerID, self.Codename)
	

def show_splash_screen():
	global splash_screen_image
	# define title of the application
	root.title("test")
	# define size of the window -> in the future add autoamatic adjustment to the user resolution
	root.geometry("1000x800")
		
	# to hide menu during splash screen
	root.overrideredirect(True)

def main_window():
    # destroying splash screen
	root.destroy()

    # creating main screen
	main_root = tk.Tk()
	main_root.title("test application")
	main_root.geometry("850x800")
	
	
	team1_container=Frame(main_root, relief="sunken", borderwidth=2)
	team1_container.pack(side="left", fill="x")
	
	team2_container=Frame(main_root, relief="sunken", borderwidth=2)
	team2_container.pack(side="left", fill="x")
	
	#create 10 players for each team
	
	for x in range(10):
		team1 = playerEntry(team1_container)
	
	for x in range(10):
		team2 = playerEntry(team2_container)
	


	

	


show_splash_screen()
root.after(300, main_window)


tk.mainloop()