from constants import *

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDRESS)

clients = set()
clients_lock = threading.Lock()

def handle_clients(connection, address):
	print(f'NEWCONNECTION ON {address} is Connected')
	try:
		connected = True
		while connected:
			message = connection.recv(1024).decode(FORMAT)
			if not message:
				print('Connection Error!')
				break
			if message == DISCONNECT_MESSAGE:
				connected = False
			print(f'{address}, {message}')
			with clients_lock:
				for c in clients:
					c.sendall(f'{address}, {message}'.encode(FORMAT))
	finally:
		with clients_lock:
			clients.remove(connection)
		connection.close()

def start():
	print(f'Server Started!')
	server.listen()
	while True:
		connection, address = server.accept()
		with clients_lock:
			clients.add(connection)
		thread = threading.Thread(target=handle_clients,
								  args=(connection, address))
		thread.start()

start()