# -*- coding: utf-8 -*-
import socket
import time
from read_sht10 import main2
from read_sht10 import test_sht1x
    
HOST = '200.1.1.229'
PORT = 8085

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen(10)
conn, addr = server.accept()
print("connected")
serverMessage = 'START'
serverMessage = serverMessage+'\n'
conn.sendall(serverMessage.encode())
conn.close
while True:
    hu1 = test_sht1x(12, 11)
    hu2 = test_sht1x(13, 15)
    hu3 = test_sht1x(16, 18)
    hu4 = test_sht1x(22, 24)
    conn, addr = server.accept()
    print('humidity:'+str(hu1)+";"+str(hu2)+";"+str(hu3)+";"+str(hu4))
    serverMessage = 'humidity:'+str(hu1)+";"+str(hu2)+";"+str(hu3)+";"+str(hu4)
    conn.sendall(serverMessage.encode())
    conn.close()

# for i in range(100):
#     serverMessage = str(i)
#     serverMessage = serverMessage+'\n'
#     conn.sendall(serverMessage.encode())
#     conn.close()
