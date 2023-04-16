
import socket
import threading
from mttkinter import mtTkinter as tk
import database
import tkinter as tk
from tkinter import *
from pygame import mixer
import random

from PIL import ImageTk, Image
import constants as config

# TkInter's instance
root = tk.Tk()

class MusicPlayer:
	def __init__(self):
		mixer.init()

	def random_song(self):
		random_track = random.randrange(1,9)
		song_play = f"../audio/Track0{random_track}.mp3"
		mixer.music.set_volume(0.5)
		mixer.music.load(song_play)
		mixer.music.play()


class Player:
	def __init__(self, PlayerID, codename):
		self.PlayerID = PlayerID
		self.codename = codename
		self.score = 0


class Team:

	def __init__(self, team_color):
		self.container = Frame(GUI.player_entry_root,
							   relief="sunken", borderwidth=2)
		self.container.pack(side="left", fill="x")
		self.color = team_color
		team_text = team_color + " Team"

		self.label = Label(self.container, text=team_text, bg=team_color)
		self.label.pack(side="top")


class CountdownScreen:
	def __init__(self):
		self.master = tk.Tk()
		self.master.title = "Loading.."
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
			timer_image_resized = timer_image_open.resize(
				(900, 800), Image.LANCZOS)
			self.timer_image = ImageTk.PhotoImage(timer_image_resized)
			label_timer_screen = tk.Label(image=self.timer_image)
			label_timer_screen.place(x=0, y=0)
			self.master.after(1000, self.start_countdown)
		else:
			self.master.destroy()
			Player_action_screen().new_window()


class Player_action_screen:
	play_action = None
	timer_label = None

	left_frame = None
	right_frame = None

	greenScore = 0
	redScore = 0

	red_team = []
	green_team = []
	game_time = 360

	def __init__(self):
		self.sock = socket.socket(socket.AF_INET,  # Internet
								  socket.SOCK_DGRAM)  # UDP
		self.sock.bind((config.SERVER_IP, int(config.PORT)))
		self.music = MusicPlayer()

	def initialize_window(self):
		# Makes the actual window
		Player_action_screen.play_action = tk.Tk()
		Player_action_screen.play_action.title("Play Action")
		Player_action_screen.play_action.geometry("400x400")

		timer_frame = Frame(Player_action_screen.play_action,
							relief="sunken", borderwidth=2)
		timer_frame.pack(side="top", pady=40)

		Player_action_screen.timer_label = Label(timer_frame)
		Player_action_screen.timer_label.pack()

	def set_left_frame(self):
		Player_action_screen.left_frame = Frame(
			self.big_frame, relief="sunken", borderwidth=2)
		Player_action_screen.left_frame.pack(side="left", padx=40)

		red_team = Label(Player_action_screen.left_frame,
						 text="Red Team", bg="red")
		self.red_team_score = Label(Player_action_screen.left_frame, text="0")

		red_team.pack(side="top")
		self.red_team_score.pack(side="top")

		Player_action_screen.leftPlayerFrame = Frame(
			Player_action_screen.left_frame, relief="sunken", borderwidth=2)
		Player_action_screen.leftPlayerFrame.pack(side="bottom")

	def set_right_frame(self):
		Player_action_screen.right_frame = Frame(
			self.big_frame, relief="sunken", borderwidth=2)
		Player_action_screen.right_frame.pack(side="right", padx=40)

		green_team = Label(Player_action_screen.right_frame,
						   text="Green Team", bg="green")
		self.green_team_score = Label(
			Player_action_screen.right_frame, text="0")

		green_team.pack(side="top")
		self.green_team_score.pack(side="top")

		Player_action_screen.rightPlayerFrame = Frame(
			Player_action_screen.right_frame, relief="sunken", borderwidth=2)
		Player_action_screen.rightPlayerFrame.pack(side="bottom")

	def countdown(self):

		if self.game_time == 0:
			Player_action_screen.timer_label['text'] = "Game is over"
		else:
			Player_action_screen.timer_label['text'] = f'Time left: {self.game_time} seconds'
		self.game_time -= 1
		if self.game_time >= 0:
			Player_action_screen.timer_label.after(1000, self.countdown)


	def receive_data(self):
		while self.game_time > 0:
			data, addr = self.sock.recvfrom(1024)  # buffer size is 1024 bytes
			decodedData = data.decode('utf-8')
			print("decodedData: " + decodedData)
			self.updateScores(data.decode('utf-8'))

	def runUdpServer(self):
		t = threading.Thread(target=self.receive_data, args=())
		t.daemon = True
		t.start()

	def new_window(self):
		self.initialize_window()

		self.big_frame = Frame(
			Player_action_screen.play_action, relief="sunken", borderwidth=2)
		self.big_frame.pack(side="bottom", pady=50)

		self.set_left_frame()
		self.set_right_frame()

		self.music.random_song()
		
		for x in self.red_team:
			codename = getattr(x, "codename")
			
			
			#Organizes the players within the PlayerFrame from top to bottom
			frame = Frame(Player_action_screen.leftPlayerFrame, borderwidth = 2)
			frame.pack()
			
			#Associates the player codename label and score label with a player object
			x.codename_label = Label(frame, text = codename)
			x.codename_label.pack(side = "left")
			
			x.score_label = Label(frame, text = "0")
			x.score_label.pack(side = "right")
			
			
		for x in self.green_team:
			codename = getattr(x, "codename")
			
			#Organizes the players within the PlayerFrame from top to bottom
			frame = Frame(Player_action_screen.rightPlayerFrame, borderwidth = 2)
			frame.pack()
			
			
			x.codename_label = Label(frame, text = codename)
			x.codename_label.pack(side = "left")
			
			x.score_label = Label(frame, text = x.score)
			x.score_label.pack(side = "right")
			
		
		self.countdown()
		self.gameEnd = False
		
		
		self.updateScores("123:123")
		
		##This is what we need to implement, something like this
		#while(self.gameEnd != True):
			##if message recieved, update scores
			#pass
		
		

	def add_active_player (self, team, id, codename):
		player_to_add = Player(id, codename)
		if team.color == "Red":
			self.red_team.append(player_to_add)
		elif team.color == "Green":
			self.green_team.append(player_to_add)
			
	def updateScores(self, udpMessage):
		
		#Gets both the player Ids in the message and puts them in a list
		actions = udpMessage.split(":")

		for x in self.red_team:
			#Checks to see which player got a hit
			if (x.PlayerID == actions[0]):
			#Checks to make sure the hit player was a green player
				for y in self.green_team:
					if(y.PlayerID == actions[1]):
						x.score += 10
						Player_action_screen.redScore += 10
						#updates score and score label
						x.score_label["text"] = x.score
						self.red_team_score["text"] = Player_action_screen.redScore
			
		for x in self.green_team:
			#Checks to see which player got a hit
			if (x.PlayerID == actions[0]):
			#Checks to make sure the hit player was a red player
				for y in self.red_team:
					if(y.PlayerID == actions[1]):
						x.score += 10
						Player_action_screen.greenScore += 10
						#updates score and score label
						x.score_label["text"] = x.score
						self.green_team_score["text"] = Player_action_screen.greenScore
			




#Creates a single player entry box
class playerEntry:

	def __set_frame(self):
		pass
		self.frame = Frame(self.team.container, relief="sunken", borderwidth=2)
		self.frame.pack(side="top")

		p_num_label = Label(self.frame, text=self.playernum)
		p_num_label.pack(side="left")

	def __set_id_frame(self):
		id_label = Label(self.frame, text="Player ID:")
		id_label.pack(side="left")

		self.id_entry = Entry(self.frame)
		self.id_entry.pack(side="left")

		self.id_button = Button(self.frame, text=">", command=self.get_player)
		self.id_button.pack(side="left")

	def __set_codename_frame(self):
		self.codename_button = Button(
			self.frame, text=">", command=self.new_codename, state="disabled")
		self.codename_button.pack(side="right")

		self.codename_entry = Entry(self.frame)
		self.codename_entry.pack(side="right")

		self.codename_label = Label(self.frame, text="Codename:")
		self.codename_label.pack(side="right")

	def __init__(self, team, playernum):

		self.PlayerID = None
		self.Codename = None
		self.team = team
		self.playernum = playernum

		self.__set_frame()

		self.__set_id_frame()
		self.__set_codename_frame()

	def __disable_id_entry(self):
		self.id_entry.config(state="disabled")
		self.id_button.config(state="disabled")

		self.codename_button.config(state="active")

	def __disable_codename_entry(self):
		# Disable entering a codename, as this is fetched from database
		self.codename_entry.insert(0, self.Codename)

		self.codename_entry.config(state="disabled")
		self.codename_button.config(state="disabled")

	def get_player(self):

		self.PlayerID = self.id_entry.get()
		self.__disable_id_entry()

		# If player already exists in database, get the codename
		# If the player does not exist, player ID is added to the database
		if (database.check_player(self.PlayerID)):

			self.Codename = database.get_codename(self.PlayerID)
			self.__disable_codename_entry()
			print(self.Codename)

			Player_action_screen.add_active_player(
				Player_action_screen, self.team, self.PlayerID, self.Codename)
		else:
			database.insert_id(self.PlayerID)

	def new_codename(self):
		self.Codename = self.codename_entry.get()
		self.codename_entry.config(state="disabled")
		# Update the codename of the corresponding id in the database
		database.insert_codename(self.PlayerID, self.Codename)
		Player_action_screen.add_active_player(
			Player_action_screen, self.team, self.PlayerID, self.Codename)


class GUI:
	player_entry_root = None

	def __init__(self):
		self.splash_screen_image = None
		self.splash_screen_address = "../assets/logo.jpg"

	def set_splash_screen_image(self):
		# Opens and resizes the image.
		splash_screen_open = Image.open(self.splash_screen_address)
		splash_screen_resized = splash_screen_open.resize(
			(1000, 800), Image.LANCZOS)
		self.splash_screen_image = ImageTk.PhotoImage(splash_screen_resized)

	def show_splash_screen(self):
		# global splash_screen_image #needs to be handled by a class
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

	def startGameShortcut(self, event):
		if event.keysym == "F5" and event.state == 0:
			GUI.player_entry_root.destroy()
			CountdownScreen()
		elif event.keysym == "F5":
			GUI.player_entry_root.destroy()
			CountdownScreen()

	def create_teams(self):
		# Create team object for each team.
		red_team = Team("Red")
		green_team = Team("Green")

		# create 15 players for each team
		for x in range(15):
			playerEntry(red_team, x+1)
			playerEntry(green_team, x+1)

	def player_entry_window(self):
		# destroying splash screen
		root.destroy()

		# creating player_entry screen
		GUI.player_entry_root = tk.Tk()
		GUI.player_entry_root.bind("<KeyPress>", self.startGameShortcut)
		GUI.player_entry_root.title(config.SCREEN_NAME_PLAYER)
		GUI.player_entry_root.geometry("900x800")

		self.create_teams()
