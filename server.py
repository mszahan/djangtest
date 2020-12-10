# https://docs.python.org/3/howto/sockets.html
# https://stackoverflow.com/questions/8627986/how-to-keep-a-socket-open-until-client-closes-it
# https://stackoverflow.com/questions/10091271/how-can-i-implement-a-simple-web-server-using-python-without-using-any-libraries

from socket import *
def creat_server():
    """docstring for creat_server"""
    serversocket = socket(AF_INET,SOCK_STREAM)
    try:
        serversocket.bind(('localhost',9000))
        serversocket.listen(5)
        while (1):
            (clientsocket, address ) = serversocket.accept()
            rd = clientsocket.recv(500).decode()
            piece = rd.split("\n")
            if len(piece)>0:
                print(piece[0])
            data = "HTTP/1.1 200 ok \r\n"
            data += "content-type:text/html; charset:utf-8 \r\n"
            data += "\r\n"
            data += "<html><body> Hello World<body><html> \r\n"
            clientsocket.sendall(data.encode())
            clientsocket.shutdown(SHUT_WR)
    except KeyboardInterrupt:
        print("\n Shutting Down \n")
    except Exception as exc:
        print("Error\n")
        print(exc)
    serversocket.close()
print("Access http://localhost:9000")
creat_server()