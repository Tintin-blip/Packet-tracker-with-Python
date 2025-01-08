from scapy.all import *
from scapy.layers.inet import IP, UDP
from scapy.layers.dns import DNS, DNSQR
import socket
import whois

## This section is about RDNS. It Only work to get DOMAIN NAMES from a IP address or range an IP address.
##
##
##
##

#https://datatracker.ietf.org/doc/html/rfc1912
def build_query(ip):
   # 1. Reversing IP to add '.in-addr.arpa'

    ip_parts = ip.split('.') 
    reversed_ip = '.'.join(reversed(ip_parts)) + '.in-addr.arpa'

    # 2. Building Dns HEADER SECTION
    packet_identifier = struct.pack('>H', 0x1234)  # 2 BYTES 
    flags = struct.pack('>H', 0x0100) 
    question_count = struct.pack('>H', 1)  # ONE QUESTION
    answer_count = struct.pack('>H', 0)  # NO ANSWERS
    authority_count = struct.pack('>H', 0)  
    additional_count = struct.pack('>H', 0)  

    # 3. Building query section
    query_name = b''.join([bytes([len(part)]) + part.encode('utf-8') for part in reversed_ip.split('.')]) ## Convert a IP to Array of Bytes
    query_name += b'\x00' 

    query_type = struct.pack('>H', 0x0c)  # Type PTR (0x0c) FF
    query_class = struct.pack('>H', 0x01)  # Class IN (Internet)

    # 4. Building message (HEADER + QUERY)
    dns_query = (
        packet_identifier +
        flags +
        question_count +
        answer_count +
        authority_count +
        additional_count +
        query_name +
        query_type + 
        query_class
    )
    return dns_query


def send_dns_query(dns_query, dns_server="8.8.8.8", port=53, timeout=10): ## DNS GOOGLE
    # Socket UDP
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    # Set timeout
    sock.settimeout(timeout)
    
    try:
        # send RDNS
        sock.sendto(dns_query, (dns_server, port))
        
        # get response
        response,_= sock.recvfrom(512)  # The max length of socket 
        
        ## All DNS request are in bytes.
        return clean_domain(hex_to_ascii(response.hex()))  # Convert bytes of DNS response to  HEX and ASCII
    
    except socket.timeout:
        #
        print(f"Error: No se recibió respuesta del servidor DNS {dns_server} después de {timeout} segundos.")
        return None  
    
    finally:
        sock.close()



def get_domain_by_ip(ip):
    packet = IP(dst=ip) / UDP()/ DNS(rd=1, qd=DNSQR(qname="www.google.com",qtype="PTR"))
    response = sr1(packet,timeout=10)

    if response: 
        print(response[DNS].summary())
        print(response[DNS])
__all__ = ['get_domain_by_ip']


def get_domain_by_ip_socket(ip):
    try:
        domain = socket.gethostbyaddr(ip)
        if domain: 
            return domain[0]
    except:
        return 0    
def get_domain_by_ip_whois(ip):
    try:
        domain = whois.whois(ip)
        return domain['domain_name']
    except:
        return 0




def hex_to_ascii(hex_list):
    # Convert each HEX byte pair to a ASCII character, only if it is print
    ascii_string = ''.join(
        chr(int(hex_list[i:i+2], 16)) if 32 <= int(hex_list[i:i+2], 16) <= 126 else '' 
        for i in range(0, len(hex_list), 2)
    )
    return ascii_string



def clean_domain(domain):
    
    # Convert domain to lowercase
    domain = domain.lower()
    
    # Search for the string 'addr arpa' and delete all text before it.
    match = re.search(r'addrarpa', domain)
    if match:
        # Mantiene todo lo que viene después de 'addrarpa'
        domain = domain[match.start():]
    
    return domain


def listOfDomain(ips): # Requiere una lista de IP unicamente
    domainBySocketDnsGoogle = []
    for ip in ips:
        try:
            query = build_query(ip)
            domain = send_dns_query(query)
            domainBySocketDnsGoogle.append(domain)
        except Exception as e:
            print(f"Error al resolver {ip}: {e}")
    return domainBySocketDnsGoogle