import socket

class server:
    def __init__(self,ip,port):
        self.Server_Socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        self.ip=ip
        self.port=port


    def start(self):

        self.Server_Socket.bind((self.ip, self.port))
        self.Server_Socket.listen()
        print(" the Server is Listening....... ")
        Client_socket, IP_PORT = self.Server_Socket.accept()
        print(Client_socket)
        print(f" The client with IP and PORT {IP_PORT} is Connected ")

        flag= True
        while flag:
            command = input ("enter command: PROCESS/ NAME/ DRIVE/ EXIT")
            Client_socket.send(command.encode())
            print(Client_socket.recv(1024).decode())

            if Client_socket.recv(1024).decode() == "disconnecting":
                break

        Client_socket.close()





t1= server("172.20.148.227",443)
t1.start()