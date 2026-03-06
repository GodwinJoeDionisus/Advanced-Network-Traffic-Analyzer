from scapy.all import sniff, IP, TCP, UDP
import sqlite3
import datetime
import os

# Get project root directory
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Database path
db_path = os.path.join(BASE_DIR, "database", "traffic.db")

conn = sqlite3.connect(db_path, check_same_thread=False)
cursor = conn.cursor()

# -----------------------------
# Traffic Table
# -----------------------------
cursor.execute("""
CREATE TABLE IF NOT EXISTS traffic (
    time TEXT,
    src_ip TEXT,
    dst_ip TEXT,
    protocol TEXT,
    length INTEGER
)
""")

conn.commit()

# -----------------------------
# Alerts Table
# -----------------------------
cursor.execute("""
CREATE TABLE IF NOT EXISTS alerts (
    time TEXT,
    source_ip TEXT,
    alert_type TEXT
)
""")

conn.commit()


def process_packet(packet):

    if packet.haslayer(IP):

        src = packet[IP].src
        dst = packet[IP].dst
        length = len(packet)

        if packet.haslayer(TCP):
            proto = "TCP"
        elif packet.haslayer(UDP):
            proto = "UDP"
        else:
            proto = "OTHER"

        timestamp = str(datetime.datetime.now())

        # Insert traffic record
        cursor.execute(
            "INSERT INTO traffic VALUES (?,?,?,?,?)",
            (timestamp, src, dst, proto, length)
        )

        conn.commit()

        # -----------------------------
        # Suspicious Traffic Detection
        # -----------------------------
        cursor.execute("""
        SELECT COUNT(*) FROM traffic
        WHERE src_ip = ?
        """, (src,))

        packet_count = cursor.fetchone()[0]

        if packet_count > 300:

            cursor.execute(
                "INSERT INTO alerts VALUES (?,?,?)",
                (timestamp, src, "High Traffic Detected")
            )

            conn.commit()

            print(f"⚠ ALERT: High traffic detected from {src}")

        # Print packet info
        print(f"{src} -> {dst} | {proto} | {length}")


print("Starting packet capture...\n")

sniff(prn=process_packet, store=False)