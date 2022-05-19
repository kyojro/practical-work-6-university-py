import socket
import psutil

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(("127.0.0.1", 2000))
i = 0
while True:
    while i < 1:
        i += 1
        client.send(f"cpu = {psutil.cpu_percent(4)}".encode("utf-8"))
        client.send(f"ram = {psutil.virtual_memory()[2]}".encode("utf-8"))
