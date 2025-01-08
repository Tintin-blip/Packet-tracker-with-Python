from scapy.all import  *
from psutil import net_if_addrs
from pprint import pprint
from ipaddress import ip_address, AddressValueError


def get_interfaces(): ## This function only request the interfaces available and group it in array of objects
    interfaces = get_working_ifaces()
    wifi = []
    ethernet = []
    wifi_keywords = ["wlan", "wi-fi", "wifi"] ## Filters to Windows and Mac
    ethernet_keywords = ["eth","eth0","eth1", "en", "ethernet"] ## Filters to Windows and Mac
    for iface in interfaces:
        iface_name = str(iface.name) 
        if any(keyword in iface_name.lower() for keyword in wifi_keywords):
            wifi.append(iface_name)
        elif any(keyword in iface_name.lower() for keyword in ethernet_keywords):
            ethernet.append(iface_name)
    return {"wifi": wifi, "ethernet": ethernet}



def is_valid_ip(ip): ## This function 
    try: 
        addr = ip_address(ip)
        return not (addr.is_multicast or addr.is_private)
    except AddressValueError:
        return False


