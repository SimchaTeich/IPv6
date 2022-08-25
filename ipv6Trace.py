from scapy import *
from scapy.layers.inet import ICMP, IP
from scapy.layers.inet6 import IPv6, ICMPv6EchoRequest
from scapy.sendrecv import send, sniff, sr1,sr

#sniff(filter='ICMP', prn=fuckoff)
def ipv4Calculate(parts):
    if (len(parts[1]) < 4):
        parts[1] = ('0' * (4 - len(parts[1]))) + parts[1]
    if (len(parts[2]) < 4):
        parts[2] = ('0' * (4 - len(parts[2]))) + parts[2]
    result = []
    result.append(parts[1][0:2])
    result.append(parts[1][2:4])
    result.append(parts[2][0:2])
    result.append(parts[2][2:4])
    finalResult = ""
    for j in range(0, 4):
        # print(result[j])
        result[j] = int(result[j], 16)
        finalResult += str(result[j]) + '.'
    return finalResult[:-1]


x = ICMPv6EchoRequest()
t = IPv6()
ipInput = '2606:4700:20::ac43:4818'
#t.dst = "172.67.72.24"
t.dst = ipInput

#t.ttl = 3
#x.show()
# x.id = 1
# x.seq = 1
r = t/x
r.show()
send(r)

for i in range(1,65):
    print(f"hlim: {i}")
    t.hlim = i
    r = t/x
    p = sr1((r), timeout = 15)
    if p is None:
        print('no response')
    else:
        print(p[IPv6].src)
        parts = p[IPv6].src.split(':')
        ipv4 = ipv4Calculate(parts)

        if(parts[0] == '2002'):
            print("ip6 to 4 tunneling detected, equivilient ipv4:")
            print(f"ipv4: {ipv4}")

        if p[IPv6].src == ipInput:
            break
    print("-------------------\n")
