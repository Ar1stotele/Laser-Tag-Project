#pip install psycopg2 first
import psycopg2

class Database:
    def __init__(self):
        self.conn = psycopg2.connect('')

    def connect(self):
        # Contains the database info, and attempts to connect to Supabase.
        # Needs Supabase info
        DB_NAME = ""
        DB_USER = ""
        DB_PASS = ""
        DB_HOST = ""
        DB_PORT = ""


        try:
            self.conn = psycopg2.connect(database = DB_NAME, user = DB_USER,
                                    password = DB_PASS, host = DB_HOST,
                                    port = DB_PORT)
            print("Database connected successfully.")
        except:
            print("Error: Database not connected.")

    def create_table(self):
        # Unfinished, I don't think this will create a working table.
        cur = self.conn.cursor()
        cur.execute ("""

        CREATE TABLE Player

        """)
    
    def add_player (self, player_add):
        # Unfinished. player_add needs to be added to the table properly.
        pass