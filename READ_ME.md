
# 🛡️ ARP Spoofing Detection & Mitigation Toolkit

This repository provides a **Python-based toolkit for ARP spoofing detection and mitigation** using **Scapy**. The system is designed for **Kali Linux** but can be run on any Unix-based machine with **root privileges**.

It includes **three independent scripts**:

- **`arpspoof.py`** – Simulates an ARP spoofing attack (for controlled testing purposes only)  
- **`detector.py`** – Monitors ARP traffic to detect potential spoofing attempts  
- **`mitigator.py`** – Sends corrective ARP responses to neutralize spoofed entries

---

## 🖥️ Deployment Scenarios

This toolkit supports **two primary use cases**:

### 🔹 Scenario A: Self-Protection (Defend Own Machine)

- **Device A** runs both `detector.py` and `mitigator.py`  
- **Device B** runs `arpspoof.py` to launch an ARP spoofing attack against **Device A**

---

### 🔹 Scenario B: Network Protection (Defend Others)

- **Device A** runs `detector.py` and `mitigator.py` to protect the network  
- **Device B** is the attacker  
- **Device C** is the victim, protected by **Device A**

---

## ⚙️ Configuration Guide

### `arpspoof.py` (Attacker)

interface = "eth0"                # Use `ifconfig` or `ip a` to identify your network interface
victim_ip = "192.168.1.38"        # IP of the target victim device
gateway_ip = "192.168.1.1"        # IP of the router/gateway
victim_mac = "b4:8c:9d:31:cb:ef"  # MAC of the victim (find using `arp -n` or `ip neigh`)

---

### `detector.py` (Defender)

known_macs = {
    "192.168.1.1": "aa:bb:cc:dd:ee:ff",   # Real MAC of the router
    "192.168.1.38": "b4:8c:9d:31:cb:ef"   # Real MAC of the victim (or self if self-protecting)
}
interface = "eth0"  # Replace with your actual network interface

---

### `mitigator.py` (Defender)

TRUSTED_MACS = {
    "192.168.1.1": "aa:bb:cc:dd:ee:ff"   # Router's genuine MAC
}
VICTIM_IP = "192.168.1.38"  # Device to protect (your own IP if defending yourself)
interface = "eth0"          # Adjust according to your setup

---

## 🛠️ Setup Instructions

1. **Install dependencies:**

sudo apt update
sudo apt install python3-pip net-tools
pip3 install scapy

2. **Make scripts executable (optional):**

chmod +x *.py

3. **Run each script (in separate terminals, as root):**

sudo python3 detector.py
sudo python3 mitigator.py
sudo python3 arpspoof.py  # attacker only

---

## ✅ Verifying the System

- Use `arp -n` or `ip neigh` to check ARP tables on the victim.
- If the MAC address for the gateway changes frequently, spoofing is active.
- If `mitigator.py` is running, the correct MAC will be restored repeatedly.
- `detector.py` will log alerts like:

[!] ARP Spoofing Detected: 192.168.1.1 claiming MAC 08:00:27:12:34:56, expected aa:bb:cc:dd:ee:ff

---

## ⚠️ Important Notes

- All scripts require **root access** due to raw packet handling.
- Only run `arpspoof.py` in **controlled environments**—do not test on public or unauthorized networks.
- Keep `mitigator.py` running continuously to defend against persistent ARP spoofing attempts.

---

## 📄 License

This project is for **educational and research purposes only**. Use responsibly.

