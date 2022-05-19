import socket
import logging
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(("127.0.0.1", 2000))
server.listen(10)

while True:
    user, address = server.accept()
    print("connect ", user.getpeername())
    user.send("connect".encode("utf-8"))
    while True:
        data = user.recv(1024).decode("utf-8").lower()
        print("user_send: ", data)
        if float(data[7]) > 70:
            logging.basicConfig(level=logging.INFO, filename='info.log', filemode='a',
                                format='%(levelname)s - %(message)s')
            logging.info(f'user: {user} CPU usage: {data[2]} \n')
