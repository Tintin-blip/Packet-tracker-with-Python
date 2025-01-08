from scapy.all import *
from scapy.all import sniff
from scapy.layers.inet import IP, TCP,UDP
from scapy.layers.l2 import Ether
from json import *
from pprint import pprint
from DNS_TOOLS import listOfDomain
from FEATURES.work_list import get_interfaces,is_valid_ip
from FEATURES.protocols import identify_protocol
from FEATURES.graphics import ipUsed
import datetime
conf.promisc = True


packetsAnalizet = []


def packet_callback(packet):

    
    if packet.haslayer(IP): ## Header IP
        info = {
            "ip": packet[IP].dst,
            "ipsrc": packet[IP].src,
            "flagSrc": packet[IP].flags,
            "id":packet[IP].id,
            "ttl":packet[IP].ttl,
            "protocol": identify_protocol(packet[IP].proto)

        }

        if packet.haslayer(TCP): ## Layer TCP
            info.update({
                "sourcePort": packet[TCP].sport,
                "destiny": packet[TCP].dport,
                "flagDest": packet[TCP].flags,

                
            })
        if packet.haslayer(UDP): ## LAYER UDP
            info.update({
                "sourcePort": packet[UDP].sport,
                "destiny": packet[UDP].dport,
            })

        info.update({
            "date":datetime.datetime.now()
        })
        if info not in packetsAnalizet:
            packetsAnalizet.append(info)
            print(f" ID:{info.get('id')},{info['ipsrc']} > {info['ip']} Flags: {info.get('flagDest', 'N/A')} Port: {info.get('sourcePort', 'N/A')} -> {info.get('destiny', 'N/A')} Protocol:{info.get('protocol')} TTL:{info.get('ttl')}, date: {info.get('date')}")


interfaces = get_interfaces()   
if 'ethernet' in interfaces and interfaces['ethernet']:
    interface = interfaces['ethernet']
elif 'wifi' in interfaces and interfaces['wifi']:
    interface = interfaces['wifi']
else:
    print('NO HAY INTERFACES DISPONIBLES')
    exit(1)

print('Interfaz usada',interface)
print("Capturando paquetes...")
sniff( count=500,timeout=10, iface=interface[0], prn=packet_callback)



ips = [data['ip'] for data in packetsAnalizet if is_valid_ip(data['ip'])]


print("\nIPs válidas capturadas:")
pprint(ips)

## This section is not necessary to capture packets. But with this code we could get domain name of all IP that we've captured
 
domains = listOfDomain(ips) 

print("\nResumen de dominios resueltos:")

pprint(domains)

