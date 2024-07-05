# Prasunet task 5 network packet sniffer

#importing all required libraries

from scapy.all import sniff, IP, Raw, conf
from scapy.layers import http


# listing the different interfaces to select the connection

def list_interfaces():
    interfaces = conf.ifaces
    for index, iface in enumerate(interfaces.values()):
        print(f"{index}: {iface.name}")
    return list(interfaces.values())

# get the number of reqruired connection

def get_interface(interfaces):
    while True:
        try:
            iface_index = int(input("Select the interface number to sniff on: "))
            if 0 <= iface_index < len(interfaces):
                return interfaces[iface_index].name
            else:
                print("Invalid interface number. Please try again.")
        except ValueError:
            print("Please enter a valid number.")

# process the packet to get source and destination ip addresses, protocol, url and payload when available
def process_packet(packet):
    if packet.haslayer(IP):
        src_ip = packet[IP].src
        dst_ip = packet[IP].dst
        protocol = packet[IP].proto

        print(f"[+] Packet: {src_ip} -> {dst_ip} (Protocol: {protocol})")

        if packet.haslayer(http.HTTPRequest):
            url = packet[http.HTTPRequest].Host.decode() + packet[http.HTTPRequest].Path.decode()
            print(f"    [HTTP Request] URL: {url}")

        if packet.haslayer(Raw):
            payload = packet[Raw].load.decode(errors='ignore')
            print(f"    [Payload] {payload}")

# main program

interfaces = list_interfaces()
iface = get_interface(interfaces)
sniff(iface=iface, store=False, prn=process_packet)
