import socket
import logging


class Server:
    def __init__(self, opt_1, opt_2):
        # socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.user = None
        self.server = socket.socket(opt_1, opt_2)

    def connect_server(self, ip, port, count_l):
        # "127.0.0.1", 2000
        self.server.bind((ip, port))
        # 10
        self.server.listen(count_l)

    def work_server(self):
        while True:
            self.user, address = self.server.accept()
            print("connect ", self.user.getpeername())
            self.user.send("connect".encode("utf-8"))
            while True:
                data = self.user.recv(1024).decode("utf-8").lower()
                print("user_send: ", data)
                if "cpu" in data and float(data.split("'")[1]) > 0.5:
                    logging.basicConfig(level=logging.INFO, filename='info.log', filemode='w',
                                        format='%(levelname)s - %(message)s')
                    d = data.split("'")[1]
                    logging.info(f"user: {self.user} CPU usage: {d}")


server = Server(socket.AF_INET, socket.SOCK_STREAM)
server.connect_server("127.0.0.1", 2000, 10)
server.work_server()
