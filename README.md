# Packet tracker with Python

## tracker.py
this script capture all packets in your local network. TCP/UDP/ICMP etc
Filter local ip address and send a Reserve Domain Name Server (RDNS) to find the domain of a scanned IP address 

## ARP.py
This script send a ARP packet to ALL ip 192.168.0.1/24 (usually used on local networks), once this is complete, it print in your terminal all IPs address connected on your local network


## main.py 
Not working



## Caution
The scripts 'tracker.py' and 'ARP.py' work with a function to obtain an interface to receive or send packets. This function prioritizes an Ethernet interface. 
If an error occurs, change it manually as follows:

![image](https://github.com/user-attachments/assets/91d577bd-085c-4411-8a69-e942ebfdfbb1)



![image](https://github.com/user-attachments/assets/64605a6e-7753-41c6-9f80-a58812f01f4d)


or 

![image](https://github.com/user-attachments/assets/a4d9f196-89ed-4279-83bd-3e9a7d349a91)

