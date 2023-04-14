from dotenv import dotenv_values

CONFIG = dotenv_values("../.env")

SERVER_IP = CONFIG.get('SERVER_IP')
PORT = CONFIG.get('PORT')
SUPERBASE_PUBLIC_KEY = CONFIG.get('SUPERBASE_PUBLIC_KEY')
SUPERBASE_PRIVATE_KEY = CONFIG.get('SUPERBASE_PRIVATE_KEY')
SCREEN_NAME_SPLASH = "Splash Screen"
SCREEN_NAME_PLAYER = "Player Entry - Press F5 to start game"

APPLICATION_TITLE = "Laser Tag"
