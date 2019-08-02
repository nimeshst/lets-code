#client for our connection

from socket import *
HOST='localhost'
PORT=21567
BUFSIZ=1024
ADDR=(HOST,PORT)
while True:
    tcp_client_socket=socket(AF_INET,SOCK_STREAM)
    tcp_client_socket.connect(ADDR)
    data=raw_input('>')
    if not data :
        break
    tcp_client_socket.send ('%s\r\n'% data )
    data = tcp_client_socket.recv(BUFSIZ)
    if not data:
        break
    print (data.strip())
    tcp_client_socket.close()
