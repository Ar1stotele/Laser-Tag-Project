
import database
import tkinter as tk
from tkinter import *
from PIL import ImageTk, Image
import constants as config

##TkInter's instance 
root = tk.Tk()




class Team:
	def __init__(self, team_color):
		self.container = Frame(GUI.player_entry_root, relief="sunken", borderwidth=2)
		self.container.pack(side="left", fill="x")
		self.color = team_color
		team_text = team_color + " Team"

		self.label = Label(self.container, text=team_text, bg = team_color)
		self.label.pack(side = "top")

class CountdownScreen:
	def __init__(self):
		self.master = tk.Tk()
		self.master.geometry("900x800")
		self.count = 30
		self.timer_image_open = None
		self.timer_image_address = ""
		self.start_countdown()
        
	def start_countdown(self):
		if self.count > 0:
			self.timer_image_address = f"../assets/countdown/{self.count}.tif"
			self.count -= 1
			timer_image_open = Image.open(self.timer_image_address)
			timer_image_resized = timer_image_open.resize((900,800), Image.LANCZOS)
			self.timer_image = ImageTk.PhotoImage(timer_image_resized)
			label_timer_screen = tk.Label(image=self.timer_image)
			label_timer_screen.place(x=0, y=0)
			self.master.after(1000, self.start_countdown)
		else:
			self.master.destroy()
			Player_action_screen.new_window(Player_action_screen)


class Player_action_screen:
	red_dict = {}
	green_dict = {}

	def new_window(self):
		#open a new window for play action screen and begin display pregame countdown
		self.play_action = tk.Tk()
		self.play_action.title("Play Action")
		self.play_action.geometry("900x800")

		left_frame = Frame(self.play_action)
		left_frame.pack(side = "left")
		right_frame = Frame(self.play_action)
		right_frame.pack(side = "right")
		timer_frame = Frame(self.play_action)
		timer_frame.pack(side = "top")
		
		for x in self.red_dict:
			red_label = Label(left_frame, text = x)
			red_label.pack()
			pass
		for y in self.green_dict:
			green_label = Label(right_frame, text = y)
			green_label.pack()
			pass
  

		timerLabel = Label(timer_frame)
		timerLabel.pack()
  
		def countdown(count):
			timerLabel['text'] = f'Time left: {count} seconds'	
			count-=1
			if count>=0:
				timerLabel.after(1000,countdown,count)

		
		time_left = 360
		countdown(time_left)
		
		

	def add_active_player (self, team, codename):
		if team.color == "Red":
			self.red_dict[codename] = 0
		elif team.color == "Green":
			self.green_dict[codename] = 0



#Creates a single player entry box
class playerEntry:

	def __init__(self, team, playernum):
	
		self.PlayerID = None
		self.Codename = None
		self.team_to_use = team
		container_to_use =  team.container
		
		self.frame = Frame(container_to_use, relief="sunken", borderwidth=2)
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

			print(self.Codename)
			Player_action_screen.add_active_player(Player_action_screen ,self.team_to_use, self.Codename)

	def newCodename(self):
		self.Codename = self.E2.get()
		self.E2.config(state = "disabled")
		#Update the codename of the corresponding id in the database
		database.insertCodename(self.PlayerID, self.Codename)
		Player_action_screen.add_active_player(Player_action_screen ,self.team_to_use, self.Codename)

	



class GUI:
	player_entry_root = tk.Tk()
	
	def __init__(self):
		self.splash_screen_image = None
		self.splash_screen_address = "../assets/logo.jpg"
		self.player_entry_root.bind("<KeyPress>", self.startGameShortcut)

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

	def player_entry_window(self):
		# destroying splash screen
		root.destroy()

		# creating player_entry screen
		self.player_entry_root.title(config.SCREEN_NAME_PLAYER)
		self.player_entry_root.geometry("900x800")

		# Create team object for each team.
		red_team = Team("Red")
		green_team = Team("Green")

		#create 19 players for each team
		for x in range(19):
			playerEntry(red_team, x+1)
			playerEntry(green_team, x+1)

		play_button = Button(self.player_entry_root, relief = "sunken", borderwidth=2, text="Lock in Teams", command = lambda: CountdownScreen()
)
		play_button.pack(side="top", pady= 40)

	def startGameShortcut(self, event):
		if event.keysym == "F5" and event.state == 0:
			CountdownScreen()
