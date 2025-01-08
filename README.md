# Packet tracker with Python

## tracker.py
this script capture all packets in your local network. TCP/UDP/ICMP etc
Filter local ip address and send a Reserve Domain Name Server (RDNS) to find the domain of a scanned IP address 

## ARP.py
This script send a ARP packet to ALL ip 192.168.0.1/24 (usually used on local networks), once this is complete, it print in your terminal all IPs address connected on your local network


## main.py 
Not working
## The script works with a virtual environment (ENV). To activate it, you must use the following command:

Being in the base folder, write:
# Windows
.\packet-tracker-with-python\Scripts\Activate
# Linux
source packet-tracker-with-python/bin/activate

![image](https://github.com/user-attachments/assets/31d0be3b-cf00-4392-bff1-3e816243f1a8)




## Caution
The scripts 'tracker.py' and 'ARP.py' work with a function to obtain an interface to receive or send packets. This function prioritizes an Ethernet interface. 
If an error occurs, change it manually as follows:

![image](https://github.com/user-attachments/assets/f7b26f86-bf8b-40f9-b812-6ec49b264330)

![image](https://github.com/user-attachments/assets/aab96f3a-f944-41b5-a95f-88e995e34f4a)

or 

![image](https://github.com/user-attachments/assets/66fcb176-7103-4058-9b7c-2df75ffa64f0)
