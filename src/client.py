from constants import *

def connect():
	client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	client.connect(ADDRESS)
	return client

def send(client, message):
	messages = message.encode(FORMAT)
	client.send(messages)

def start():
	choice = input('Do You Want to Chat?(yes or no) ') or None
	if choice.lower() != 'yes':
		return 

	connection = connect()
	while True:
		message = input('Your Message (q to Quit): ')
		if message == 'q':
			break
		send(connection, message)
	send(connection, DISCONNECT_MESSAGE)
	time.sleep(1)
	print('Dis-Connected')

start()