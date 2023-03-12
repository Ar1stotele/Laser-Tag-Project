from supabase import create_client
import supabase
import constants as config
supabase: supabase = create_client(config.SUPERBASE_PUBLIC_KEY, config.SUPERBASE_PRIVATE_KEY)

#Check if player already exists
def check_player(PlayerID):

	player = supabase.table('Players').select('*').eq("PlayerID", PlayerID).execute().data
	
	if(player):
		print("Player exists with this player ID")
		return True
	else:
		return False

#Insert a player into a database
def insert_player_id(PlayerID):

	data = {
		"PlayerID": PlayerID,
		"Codename" : "null"
	}
	
	supabase.table('Players').insert(data).execute()
	print("Added player id to database")



#Return the codename of the player using the player ID
def get_codename(PlayerID):

	player = supabase.table('Players').select('*').eq("PlayerID", PlayerID).execute().data
	codename_to_get = player[0]
	return codename_to_get["Codename"]


def insert_codename(PlayerID, Codename):
	supabase.table('Players').update({"Codename": Codename}).eq("PlayerID", PlayerID).execute()
	print("Updated Codename")

