import socket
import psutil

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(("127.0.0.1", 2000))


class Client:
    def __init__(self, opt_1, opt_2):
        self.client = socket.socket(opt_1, opt_2)

    def connect_serv(self, ip, port):
        self.client.connect((ip, port))

    @staticmethod
    def delivery():
        i = 0
        while True:
            data = client.recv(1024).decode("utf-8").lower()
            print(data)
            while i < 1:
                i += 1
                client.send(f"ram = '{psutil.virtual_memory()[2]}'".encode("utf-8"))
                client.send(f"cpu = '{psutil.cpu_percent(4)}'".encode("utf-8"))


x = Client(socket.AF_INET, socket.SOCK_STREAM)
x.connect_serv("127.0.0.1", 2000)
x.delivery()
