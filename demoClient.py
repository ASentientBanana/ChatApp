import socket
import threading
port = 3241
host = '127.0.0.1'
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect((host,port))
msgs = []



def send():
    msg = input('>> ')
    s.send(msg.encode())
        


while True:
    
    sThread = threading.Thread(target=send)
    sThread.daemon = True
    sThread.start()
    Rdata = s.recv(1024)
    msgs.append(Rdata.decode())
    print(Rdata.decode())

    