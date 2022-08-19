# Run this script from Alice machine

import socket
import time

KB = 1024

"""
BOB: Alice, I finally managed the ping6.

ALICE: really? how

BOB: My network card was in a promiscuous state, so I canceled it

ALICE: Sounds good. But now something strange is happening to me...

BOB: What do you mean strange?

ALICE: I think Eve is playing cache on me. again.

Bob: I mean she's listening to us now?!
"""

def main():
    sock = socket.socket(socket.AF_INET6, socket.SOCK_STREAM)
    sock.create_connection("fe80::1eaa:7821:6306:2979%enp0s3", 13337))
   
    print(sock.recv(KB).decode())
    sock.sendall(b"really? how")
    time.sleep(2)
    print(sock.recv(KB).decode())
    sock.sendall(b"Sounds good. But now something strange is happening to me...")
    time.sleep(2)
    print(sock.recv(KB).decode())
    sock.sendall(b"I think Eve is playing cache on me. again.")
    time.sleep(2)
    print(sock.recv(KB).decode())
    time.sleep(2)
    
    sock.close()
    
    
if __name__ == "__main__":
    main()