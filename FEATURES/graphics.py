import matplotlib.pyplot as plt
from collections import Counter


def ipUsed(ips):
    ip_counts = Counter(ips)
    
    ip_labels = list(ip_counts.keys())
    ip_frequencies = list(ip_counts.values())
    
    
    plt.bar(ip_labels, ip_frequencies, color='lightgreen', edgecolor='black')
    
    plt.xlabel('Direcciones IP')
    plt.ylabel('Frecuencia de Uso')
    plt.title('Frecuencia de Direcciones IP')
    

    plt.xticks(rotation=45)  
    plt.tight_layout()
    plt.show()

