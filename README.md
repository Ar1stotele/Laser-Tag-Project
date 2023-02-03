# Laser-Tag-Project
The main software for a laser tag system

---

Requirements for software:
- Written in your favorite language
- Needs to interface with a postgresql database
- Can use more than one window
- Need to set up 2 udp sockets for transmission of data to/from players
	- Use socket 7500 to broadcast, 7501 to receive
	- Format of transmission will be a single integer (id of player who got hit)
	- Format of received data will be integer:integer (id of player transmitting;id of player hit)
- Software displays a splash screen for 3 seconds (logo provided) upon startup
- Software will then move to a player entry screen (check screen captures for format)
	- Operator will then fill in the user id number, system will query database for code name.  If not found, allow for the entry of a new code name and then add to the database
	- After all players have been entered (max of 15 per team), pressing f5 (or a start button) will move to the next screen which is the play action screen.
- Play action screen will have 3 areas that will be constantly updating
	- There will be a count down timer for 6 minute games.  Have a 30 second warning before starting.
	- Play by play action will be shown in a window on the main screen.  The events can scroll off as the window fills.
	- Cumulative team scores will be constantly updating.
	- Individual scores will be constantly updating
	- High team score will be flashing during play
	- During gameplay a random mp3 music file will be playing (files provided by instructor)
