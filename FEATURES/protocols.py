import re
def identify_protocol(id):
    protocols = { 
        1:"ICMP",
        6:"TCP",
        17:"UDP",
        2:"IGMP",
        53:"DNS",

    }
    
    if protocols.get(id):
        return protocols.get(id)
    else: 
        return 'No protocol'
