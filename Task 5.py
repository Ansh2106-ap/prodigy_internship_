from scapy.all import sniff
from scapy.layers.inet import IP, TCP, UDP
from scapy.packet import Raw

def analyze_packet(packet):
    if IP in packet:
        src_ip = packet[IP].src
        dst_ip = packet[IP].dst
        protocol = packet[IP].proto

        print("\n==============================")
        print(f"Source IP      : {src_ip}")
        print(f"Destination IP : {dst_ip}")

        if packet.haslayer(TCP):
            print("Protocol       : TCP")
        elif packet.haslayer(UDP):
            print("Protocol       : UDP")
        else:
            print(f"Protocol       : Other ({protocol})")

        if packet.haslayer(Raw):
            payload = packet[Raw].load[:50]
            print(f"Payload (partial): {payload}")

def start_sniffing():
    print("⚠️ Packet Sniffer Started (Educational Use Only)")
    print("Press Ctrl + C to stop\n")
    sniff(prn=analyze_packet, store=False)

# -------- Main Program --------
start_sniffing()