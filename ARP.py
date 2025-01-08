from scapy.all import ARP, Ether, srp,IP,ICMP
from scapy.all import *
from src.FEATURES.work_list import get_interfaces,is_valid_ip

interfaces = get_interfaces()   

## This section is about ARP. It is used to obtain local IP adress on a  local network
## Local IP adress are used to use to identify a packets with a IP address

if 'ethernet' in interfaces and interfaces['ethernet']:
    interface = interfaces['ethernet']
elif 'wifi' in interfaces and interfaces['wifi']:
    interface = interfaces['wifi']
else:
    print('NO HAY INTERFACES DISPONIBLES')
    exit(1)

print(interfaces)

def scan_network(network):
    # Creating ARP packet
    #First, the ARP packet (Address Resolution Protocol). This resolving a MAC address and get information it.
    
    # With ARP() we're creating a ARP protocol with PDST. Pdst is the network destination, in other words the range of IP that we going to query.
    arp_request = ARP(pdst=network)

    # ARP working on local network, so we must  use a Ether Protocol (Layer 1 of TCP/IP)
    broadcast = Ether(dst="ff:ff:ff:ff:ff:ff") ## ff:ff:ff:ff:ff:ff. This is a broadcast address that targets ALL devices on local network

    packet = broadcast / arp_request # Couling two protocols. ETHER / ARP
    
    # Send a packet and receive a response     
    result = srp(packet, iface=interface[0], timeout=7, retry=5,verbose=False)[0] # iface is Interface. timeout is the time to wait for a response and retry is the number of packets per device
    
    devices = []
    for sent,received in result:
        print(received)
        devices.append({'ip': received.psrc, 'mac': received.hwsrc, 'info': received.answers})
    
    return devices

# Specifing a range of IP. 192.168.0.0/24     - 192.168.0.0 -> 192.168.0.255
network_range = "192.168.0.0/24"
print(f"Escaneando la red {network_range}...")
devices = scan_network(network_range)

print(devices)
# Show all founded devices
print("Dispositivos encontrados:")
for device in devices:
    print(f"IP: {device['ip']}, MAC: {device['mac']}")


