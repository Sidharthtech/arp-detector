from scapy.all import ARP, Ether, sendp
import time

TRUSTED_MACS = {
    "192.168.1.1": "34:56:78:9a:bc:de"
}

VICTIM_IP = "192.168.1.38"

def send_correct_arp(ip_address):
    interface = "eth0"
    correct_mac = TRUSTED_MACS.get(ip_address)

    if correct_mac:
        ether = Ether(src=correct_mac, dst="ff:ff:ff:ff:ff:ff")
        arp = ARP(
            op=2,
            psrc=ip_address,
            pdst=VICTIM_IP,
            hwsrc=correct_mac,
            hwdst="ff:ff:ff:ff:ff:ff"
        )
        packet = ether / arp
        sendp(packet, iface=interface, verbose=False)
        print(f"[+] Sent corrective ARP: {ip_address} is at {correct_mac}")

if __name__ == "__main__":
    try:
        while True:
            send_correct_arp("192.168.1.1")
            time.sleep(2)
    except KeyboardInterrupt:
        print("\n[!] Mitigation stopped.")
