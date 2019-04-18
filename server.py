import socket , threading

Port = 3241
IP = ''
server_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR,1)
server_socket.bind((IP,Port))
server_socket.listen()

connections = []

def handler(conn,connections):
    while True:
        data = conn.recv(1024)
        for i in connections:
            i.send(data)
        if not data:
           print('not data')
           conn.send(b' ending connection')
           break    

while True:
    conn,a = server_socket.accept()
    connections.append(conn)
    print(connections)
    mThread = threading.Thread(target=handler,args=(conn,connections))
    mThread.daemon = True
    mThread.start()