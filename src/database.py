from supabase import create_client
import supabase
import constants as config
supabase: supabase = create_client(config.superbase_public_key, config.superbase_private_key)


#Insert a player into a database
def getPlayerID(PlayerID):
	
	#See if the player already exists, if not, insert a new player into the database
	if(checkPlayer(PlayerID)):
		return True
	else:
		data = {
		"PlayerID": PlayerID,
		"Codename" : "null"
		}
		supabase.table('Players').insert(data).execute()
		print("Added player id to database")
		return False

#Check if player already exists
def checkPlayer(PlayerID):

	dict = supabase.table('Players').select('*').eq("PlayerID", PlayerID).execute().data
	
	if(dict):
		print("Player already exists with this player ID")
		return True
	else:
		return False
		

#Return the codename of the player using the player ID
def getCodename(PlayerID):

	dict = supabase.table('Players').select('*').eq("PlayerID", PlayerID).execute().data
	dict = dict[0]
	return dict["Codename"]


def insertCodename(PlayerID, Codename):
	supabase.table('Players').update({"Codename": Codename}).eq("PlayerID", PlayerID).execute()
	print("Updated Codename")

