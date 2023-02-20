from dotenv import dotenv_values

config = dotenv_values("../.env")

server_ip = config.get('SERVER_IP')
port = config.get('PORT')
superbase_public_key = config.get('SUPERBASE_PUBLIC_KEY')
superbase_private_key = config.get('SUPERBASE_PRIVATE_KEY')
screen_name_splash = "Splash Screen"
screen_name_player = "Player Entry"

print(server_ip)

application_title = "Laser Tag"
