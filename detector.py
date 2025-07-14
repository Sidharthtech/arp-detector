from scapy.all import sniff, ARP
from mitigator import send_correct_arp
import logging

logging.basicConfig(filename="log.txt", level=logging.INFO)
ip_mac_mapping = {}

def handle_arp_packet(packet):
    if packet.haslayer(ARP) and packet[ARP].op == 2:
        sender_ip = packet[ARP].psrc
        sender_mac = packet[ARP].hwsrc
        if sender_ip in ip_mac_mapping and ip_mac_mapping[sender_ip] != sender_mac:
            log_entry = f"ARP spoofing detected: {sender_ip} changed from {ip_mac_mapping[sender_ip]} to {sender_mac}"
            logging.warning(log_entry)
            send_correct_arp(sender_ip)
        else:
            ip_mac_mapping[sender_ip] = sender_mac

sniff(filter="arp", prn=handle_arp_packet, store=0)
