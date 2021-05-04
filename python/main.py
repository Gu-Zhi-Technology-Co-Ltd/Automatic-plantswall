# -*- coding: utf-8 -*-
import socket
import time
HOST = '200.1.1.103'
PORT = 8081

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen(10)

while True:
    conn, addr = server.accept()
    print("connected")
    serverMessage = input()
    serverMessage = serverMessage+'\n'
    conn.sendall(serverMessage.encode())
    conn.close
print('test')
# for i in range(100):
#     serverMessage = str(i)
#     serverMessage = serverMessage+'\n'
#     conn.sendall(serverMessage.encode())
#     conn.close()
