import socket, threading

Port = 3241
IP = ''

connections = []


def handler(conn, connections):
	while True:
		data = conn.recv(1024)
		for c in connections:
			# do not return the message to the same client
			if c is not conn:
				c.send(data)
		if not data:
			print('closing connection')
			conn.send(b'ending connection')
			# obivious
			connections.remove(conn)
			# print rest of the connections after removing closed one
			print([c.getpeername() for c in connections])
			break


def main():
	server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
	server_socket.bind((IP, Port))
	print(f"Server started on port {Port}")
	server_socket.listen(0)
	while True:
		conn, a = server_socket.accept()
		connections.append(conn)
		# prettier print with shorthand list notation
		print([c.getpeername() for c in connections])
		mThread = threading.Thread(target=handler, args=(conn, connections))
		mThread.daemon = True
		mThread.start()


# if you call this file  like 'python server.py' call function main()
if __name__ == "__main__":
	main()
