from flask import Flask

import os
from supabase import create_client, Client
import supabase

supabase: supabase = create_client("https://uijrqelihosqdealglud.supabase.co", "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InVpanJxZWxpaG9zcWRlYWxnbHVkIiwicm9sZSI6ImFub24iLCJpYXQiOjE2NzU4MDA1NjYsImV4cCI6MTk5MTM3NjU2Nn0.3m6URnm6uwpDxf-i-ucElMpzTfC4IHAiY-dGwgQisfQ")
app = Flask(__name__)


##data = supabase.table("countries").select("*").eq("country", "IL").execute()

data = {
    'PlayerID': 7,
    'Codename': 'Hello',
    'Score': '8200',
    
}


@app.route("/addPlayer")
def insertPlayer():
	supabase.table('Players').insert(data).execute()
	print(supabase.table('Players').select('*').execute().data)
	return "addedPlayer: " + str(data['PlayerID'])


@app.route('/')
def hello_world():
   return 'Hello Tutorialspoint'

if __name__ == '__main__':
   app.run()
   
   