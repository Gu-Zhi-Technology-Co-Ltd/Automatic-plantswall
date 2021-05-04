# -*- coding: utf-8 -*-
import socket
import time
HOST = '200.1.1.103'
PORT = 8081

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen(10)
conn, addr = server.accept()
print("connected")
while True:
    serverMessage = input()
    serverMessage = serverMessage+'\n'
    conn.sendall(serverMessage.encode())
    conn.close()
# for i in range(100):
#     serverMessage = str(i)
#     serverMessage = serverMessage+'\n'
#     conn.sendall(serverMessage.encode())
#     conn.close()