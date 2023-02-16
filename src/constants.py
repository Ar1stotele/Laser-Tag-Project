from dotenv import dotenv_values

config = dotenv_values(".env")

server_ip = config.get('SERVER_IP')
port = config.get('PORT')

application_title = "Laser Tag"

