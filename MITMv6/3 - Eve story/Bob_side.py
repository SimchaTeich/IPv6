# Run this script from Bob machine

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
    listen_sock = socket.socket(socket.AF_INET6, socket.SOCK_STREAM)
    listen_sock.bind(("::", 13337))
    listen_sock.listen(1)
    client_sock, _ = listen_sock.accept()
    
    client_sock.sendall(b"Alice, I finally managed the ping6.")
    time.sleep(2)
    print(client_sock.recv(KB).decode())
    client_sock.sendall(b"My network card was in a promiscuous state, so I canceled it")
    time.sleep(2)
    print(client_sock.recv(KB).decode())
    client_sock.sendall(b"What do you mean strange?")
    time.sleep(2)
    print(client_sock.recv(KB).decode())
    client_sock.sendall(b"I mean she's listening to us now?!")
    time.sleep(2)
    
    client_sock.close()
    listen_sock.close()
    
    
if __name__ == "__main__":
    main()