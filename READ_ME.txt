# 🛡️ ARP Spoofing Detection & Mitigation Toolkit

This project includes Python-based tools to detect and prevent ARP spoofing attacks on a local network using Scapy. It is built for Kali Linux but can run on any Unix-based system with root access. The system consists of three scripts:

- `arpspoof.py`: Launches an ARP spoofing attack (for testing purposes)
- `detector.py`: Monitors ARP packets and detects spoof attempts
- `mitigator.py`: Sends corrective ARP replies to fix spoofed entries

---

## 🖥️ Deployment Scenarios

This project supports two modes:

### 🅰️ Device A Protects **Itself**
- Device A runs both `detector.py` and `mitigator.py`
- Device B runs `arpspoof.py` and attacks Device A

### 🅱️ Device A Protects **Others**
- Device A runs `detector.py` and `mitigator.py`
- Device B is the attacker
- Device C is the victim being protected

---

## 📝 What to Change in Each Script

### `arpspoof.py` (attacker - Device B)
```python
interface = "eth0"                # Use `ifconfig` or `ip a` to find the correct one
victim_ip = "192.168.1.38"        # IP of the device being attacked
gateway_ip = "192.168.1.1"        # IP of the router
victim_mac = "b4:8c:9d:31:cb:ef"  # MAC of the victim (use `arp -n` or `ip neigh`)
```

---

### `detector.py` (defender - Device A)
```python
known_macs = {
    "192.168.1.1": "aa:bb:cc:dd:ee:ff",   # Real MAC of the router
    "192.168.1.38": "b4:8c:9d:31:cb:ef"   # Real MAC of the victim (yourself if self-protecting)
}
interface = "eth0"  # or "wlan0" depending on your device
```

---

### `mitigator.py` (defender - Device A)
```python
TRUSTED_MACS = {
    "192.168.1.1": "aa:bb:cc:dd:ee:ff"   # Router's real MAC
}
VICTIM_IP = "192.168.1.38"  # The machine to protect (your own IP if self-protecting)
interface = "eth0"          # Adjust according to your network adapter
```

---

## ⚙️ Setup Instructions

1. Install dependencies:
```bash
sudo apt update
sudo apt install python3-pip net-tools
pip3 install scapy
```

2. (Optional) Make scripts executable:
```bash
chmod +x *.py
```

3. Run each script in separate terminals as root:
```bash
sudo python3 detector.py
sudo python3 mitigator.py
sudo python3 arpspoof.py  # attacker only
```

---

## ✅ Verifying Results

- Run `arp -n` or `ip neigh` on the victim device.
- If MAC for `192.168.1.1` keeps switching, spoofing is working.
- If mitigator is active, correct MAC will keep getting restored.
- `detector.py` will print logs like:
```
[!] ARP Spoofing Detected: 192.168.1.1 claiming MAC 08:00:27:12:34:56, expected aa:bb:cc:dd:ee:ff
```

---

## 🧠 Notes

- Scripts must be run with `sudo` due to raw packet access.
- Keep mitigation running continuously to counter persistent spoofing.
- Do **not** run `arpspoof.py` on public networks — it is for controlled testing only.

---
```
