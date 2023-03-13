# Laser-Tag-Project
The main software for a laser tag system

---
How to run
	- create .env with appropriate data, .env file is pinned in Team 17 slack channel. Add this to the directory of the repo. 
	- go to directory /src
	- Run the following command "python "main.py"" to run the program.

Requirements for software:
	- Needs to interface with a postgresql database
	- Can use more than one window
	- Need to set up 2 udp sockets for transmission of data to/from players
		- Use socket 7500 to broadcast, 7501 to receive
		- Format of transmission will be a single integer (id of player who got hit)
		- Format of received data will be integer:integer (id of player transmitting;id of player hit)
	- Software displays a splash screen for 3 seconds (logo provided) upon startup
	- Software will move to a player entry screen (check screen captures for format)
		- Operator will  fill in the user id number, system will query database for code name. If not found, allow for the entry of a new code name and then add to the database
		- After all players have been entered (max of 15 per team), pressing f5 (or a start button) will move to the next screen which is the play action screen.
	- Play action screen will have 3 areas that will be constantly updating
		- There will be a count down timer for 6 minute games.  Have a 30 second warning before starting.
		- Play by play action will be shown in a window on the main screen.  The events can scroll off as the window fills.
		- Cumulative team scores will be constantly updating.
		- Individual scores will be constantly updating
		- High team score will be flashing during play
		- During gameplay a random mp3 music file will be playing (files provided by instructor)


Direction for adding new players:
	- The screen is divided into two halves for teams, each with individual lines for player entry
	- Add an ID to a line on the desired team's side, and press the arrow button to the right of the space. If a player with that ID exists, their codename will be automatically filled in next to the player ID.
	- If a player with the submitted ID does not exist yet, the codename will not be automatically filled. Fill in the codename corresponding to the ID number, and click the arrow button next to the right of the space. This codename will be saved into the database and be automatically filled next time the player ID is used.
