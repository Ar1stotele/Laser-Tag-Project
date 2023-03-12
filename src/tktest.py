
import database
import tkinter as tk
from tkinter import *
from PIL import ImageTk, Image
import constants as config


##TkInter's instance 
root = tk.Tk()

def new_window(self):
  #open a new window for play action screen and begin display pregame countdown
  self.play_action = tk.Tk()
  self.play_action.title("Play Action")
  self.play_action.geometry("900x800")



	#Frames for holding teams
  team1_container=Frame(self.play_action, relief="sunken", borderwidth=2)
  team1_container.pack(side="left", fill="x")

  team2_container=Frame(self.play_action, relief="sunken", borderwidth=2)
  team2_container.pack(side="right", fill="x")



	#Team titles
  team1Label = Label(team1_container, text="Red Team", bg = "Red")
  team2Label = Label(team2_container, text="Green Team", bg = "Green")

  team1Label.pack(side = "top")
  team2Label.pack(side = "top")

  for x in range(19):
			playerEntry	(team1_container, x+1)
			playerEntry(team2_container, x+1)

    

#Creates a single player entry box
class playerEntry:

	def __init__(self, container, playernum):
	
		self.PlayerID = None
		self.Codename = None
		
		self.frame = Frame(container, relief="sunken", borderwidth=2)
		self.frame.pack(side = "top")
		
		self.P1 = Label(self.frame, text=playernum)
		self.P1.pack(side = "left")
		
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
	

class GUI:

	def __init__(self):
		self.splash_screen_image = None
		self.splash_screen_address = "../assets/logo.jpg"

	def set_splash_screen_image(self):
		# Opens and resizes the image.
		splash_screen_open = Image.open(self.splash_screen_address)
		splash_screen_resized = splash_screen_open.resize((1000,800), Image.LANCZOS)
		self.splash_screen_image = ImageTk.PhotoImage(splash_screen_resized)

	def show_splash_screen(self):
		#global splash_screen_image #needs to be handled by a class
		# define title of the application
		root.title(config.SCREEN_NAME_SPLASH)
		# define size of the window -> in the future add autoamatic adjustment to the user resolution
		root.geometry("1000x800")
			
		# to hide menu during splash screen
		root.overrideredirect(True)
		
		self.set_splash_screen_image()

		# Creates a label with the splash screen image on it and aligns it.
		label_splash_screen = tk.Label(image=self.splash_screen_image)
		label_splash_screen.grid(column=0, row=0)

	def main_window(self):
		# destroying splash screen
		root.destroy()

		# creating main screen
		main_root = tk.Tk()
		main_root.title(config.SCREEN_NAME_PLAYER)
		main_root.geometry("900x800")
		
		#Frames for holding teams
		team1_container=Frame(main_root, relief="sunken", borderwidth=2)
		team1_container.pack(side="left", fill="x")
		
		team2_container=Frame(main_root, relief="sunken", borderwidth=2)
		team2_container.pack(side="right", fill="x")

		play_button = Button(main_root, relief = "sunken", borderwidth=2, text="Lock in Teams", command = lambda: new_window(self))
		play_button.pack(side="top", pady= 40)

		
		#Team titles
		team1Label = Label(team1_container, text="Red Team", bg = "Red")
		team2Label = Label(team2_container, text="Green Team", bg = "Green")
		
		team1Label.pack(side = "top")
		team2Label.pack(side = "top")
		
		
		#create 19 players for each team
		
		for x in range(19):
			playerEntry(team1_container, x+1)
			playerEntry(team2_container, x+1)
