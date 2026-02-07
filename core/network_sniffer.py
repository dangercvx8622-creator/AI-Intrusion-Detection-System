from scapy.all import sniff, wrpcap

def packet_callback(packet):
    # Basic filtering: Only TCP/UDP packets
    if packet.haslayer('TCP') or packet.haslayer('UDP'):
        # You can add more logic here to extract features on-the-fly
        pass

# Capture 1000 packets (adjust as needed)
packets = sniff(prn=packet_callback, count=1000, iface='eth0')  # Replace 'eth0' with your interface
wrpcap('captured_traffic.pcap', packets)
print("Captured packets saved to captured_traffic.pcap")
