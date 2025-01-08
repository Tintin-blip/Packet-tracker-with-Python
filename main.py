from scapy.all import *
from scapy.layers.inet import IP, TCP,ICMP
from scapy.layers.l2 import Ether

print('Hola')
print('')


def format(packet):
    print(packet.summary())
sniff(timeout=10,count=20,prn=format,iface='Wi-Fi')
