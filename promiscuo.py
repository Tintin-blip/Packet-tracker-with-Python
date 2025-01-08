import socket
import nmap
scanner = nmap.PortScanner(nmap_search_path=['C:\\Program Files (x86)\\Nmap\\nmap.exe'])
print(scanner)
def get_hostname(ip):
    try:
        hostname = socket.gethostbyaddr(ip)[0]
        return hostname
    except socket.herror:
        return "Hostname no encontrado"


x = get_hostname('192.168.0.102')
print(x)
