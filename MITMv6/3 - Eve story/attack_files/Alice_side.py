# Run this script from Alice machine

import socket
import time

IFACE = "enp0s3"

KB = 1024
PORT = 13337
BOB_IP = "fe80::1eaa:7821:6306:2979"
HOST = BOB_IP + "%" + IFACE
ADDR = HOST, PORT

ALICE_MSGS = ["really? how",
            "Sounds good. But now something strange is happening to me...",
            "I think Eve is playing cache on me. again."]

def main():
    sock = socket.create_connection(ADDR)
   
    for msg in ALICE_MSGS:
        time.sleep(2)
        print("Bob: " + sock.recv(KB).decode())
        time.sleep(2)
        print("Me: " + msg)
        sock.sendall(msg.encode())
    
    while True:
        pass
    
    sock.close()
    
    
if __name__ == "__main__":
    main()