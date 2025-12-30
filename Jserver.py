import socket
import json


class Server:
    def __init__(self, ip, port):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.bind((ip, port))
        self.sock.listen(1)
        self.conn, _ = self.sock.accept()

    def send_json(self, command_type, details=""):
        # יצירת מילון והפיכתו למחרוזת JSON
        data = {"cmd": command_type, "args": details}
        self.conn.send(json.dumps(data).encode())

        # קבלת תשובה (גם היא ב-JSON)
        response = self.conn.recv(4096).decode()
        return json.loads(response)

    def run(self):
        # דוגמה לשליחה
        print(self.send_json("DRIVE"))
        self.conn.close()


if __name__ == "__main__":
    Server('172.20.148.222', 443).run()