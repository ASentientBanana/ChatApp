import socket
import threading

port = 3241
host = '127.0.0.1'
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host, port))
msgs = []


def send():
	msg = input('>> ')
	s.send(msg.encode())


# Rdata = s.recv(1024)
# msgs.append(Rdata.decode())
# this way client will block until it recieves another message, solution is to open a listener thread
# to listen for incoming messages

def listener():
	while True:
		Rdata = s.recv(1024)
		msgs.append(Rdata.decode())
	    	# to avoid ">> incoming message" since ">>" is an input marker
    		print(f"\n{Rdata.decode()}")


def main():
	lThread = threading.Thread(target=listener)
	lThread.daemon = True
	lThread.start()
	while True:
		send()


# same stuff as in server.py
if __name__ == "__main__":
	main()
