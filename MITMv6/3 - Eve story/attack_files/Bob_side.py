# Run this script from Bob machine

import socket
import time

KB = 1024
PORT = 13337
HOST = "::"
ADDR = HOST, PORT

BOB_MSGS = ["Alice, I finally managed the ping6.",
            "My network card was in a promiscuous state, so I canceled it",
            "What do you mean strange?",
            "I mean she's listening to us now?!"]


def main():
    listen_sock = socket.socket(socket.AF_INET6, socket.SOCK_STREAM)
    listen_sock.bind(ADDR)
    listen_sock.listen(1)
    client_sock, _ = listen_sock.accept()
    
    for msg in BOB_MSGS:
        
        time.sleep(2)
        print("Me: " + msg)
        client_sock.sendall(msg.encode())
        time.sleep(2)
        print("Alice: " + client_sock.recv(KB).decode())
    
    while True:
        pass
    
    client_sock.close()
    listen_sock.close()
    
    
if __name__ == "__main__":
    main()