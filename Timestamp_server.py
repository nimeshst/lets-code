"""
#creatimg a tcp seerver

from socket import*
from time import ctime

HOST=''#host is kept blank which is an indicator that our server can use any address that they want 
PORT=21567
BUFSIZ=1024
ADDR=(HOST,PORT)

tcp_ser_socket=socket(AF_INET,SOCK_STREAM)#address family , connection style
tcp_ser_socket.bind(ADDR)
tcp_ser_socket.listen(5) #at a time maximum 5 client can connect

while True:
    print('waiting for connection')
    tcp_client_socket, addr=tcp_ser_socket.accept()
    print('connectied from :',addr)
    while True:
        data=tcp_client_socket.recv(BUFSIZ)#recieve TCP message 
        if not data:
            break
        tcp_client_socket.send('[%s] %s '%(bytes(ctime(),'utf-8'),data))
    tcp_client_socket.close()

tcp_ser_socket.close()
"""
#creating socket server
from SocketServer import TCPServer as TCP 
from SocketServer import StreamRequestHandler as srh
from time import ctime 

HOST=''
PORT=21567
ADDR=(HOST,PORT)#a tuple consisting of host and port

class My_request_handler(srh):#inheriting the stream request handler class 
    def handle(self):
        #handle class treats the incoming data as a file 
        #this code returns both the server and sender data 
        print('connected from',self.client_address)
        self.wfile.write('[%s]%s'%(ctime(),self.rfile.readline()))

tcp_server =TCP(ADDR,My_request_handler)
print('waiting for the connection')
#an infinite loop to serve the client requests
tcp_server.serve_forever()
