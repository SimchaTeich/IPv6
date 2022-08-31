'''this code was attempted to make viritual machines communicate with eachother while they are on DIFFERENT networks.
the purpose was to test the 6 to 4 tunnel detector, however as for the time take handover date, the attempt failed.'''

import socket

porty = 12345
p = socket.socket(socket.AF_INET6, socket.SOCK_STREAM)
p.bind(("fd17:625c:f037:2:ecd0:8972:91c1:6230",porty))
p.listen(2)
while True:
    a,b =p.accept()
    print("client connected")
    while True:
        data = a.recv(4096)
        print(str(data.decode('utf-8')))