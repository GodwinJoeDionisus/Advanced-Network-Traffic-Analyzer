# Advanced Network Traffic Analyzer with Mini IDS

A real-time **Network Traffic Analyzer and Intrusion Detection System (IDS)** built using Python.  
This project captures live network packets, analyzes traffic patterns, detects suspicious activity, and visualizes insights through a real-time web dashboard.

This project demonstrates how **network monitoring and intrusion detection systems work internally**, making it a valuable learning tool for cybersecurity and network security.

---

## Project Overview

The Advanced Network Traffic Analyzer monitors live network traffic and stores packet data for analysis.  
It provides real-time visualization and detects abnormal network behavior.

The system captures packets, processes them, stores them in a database, and provides analytics through a web dashboard.

The project simulates how **SOC (Security Operations Center) monitoring tools work**.

---

## Features

- Live packet capture using **Scapy**
- Traffic logging in **SQLite database**
- Real-time monitoring dashboard
- Protocol distribution visualization
- Top source IP analysis
- Intrusion detection alerts
- Security alerts panel
- REST API for traffic analytics
- Lightweight and easy to run locally

---

## Technologies Used

- Python  
- Scapy  
- Flask  
- SQLite  
- Chart.js  
- HTML  
- CSS  
- JavaScript  

---

## Project Architecture

```
Packet Capture (Scapy)
        ↓
Traffic Processing
        ↓
Intrusion Detection Logic
        ↓
SQLite Database
        ↓
Flask REST API
        ↓
Web Dashboard (Chart.js)
```

The architecture separates packet capture, analysis, API services, and visualization.

---

## Dashboard Capabilities

The web dashboard provides:

### Protocol Distribution
Shows the percentage of TCP, UDP, and other traffic.

### Top Source IPs
Displays the most active devices sending packets.

### Live Traffic Monitor
Shows the most recent packets captured in real-time.

### Security Alerts
Displays intrusion detection alerts such as:

```
⚠ High Traffic Detected from 192.168.1.34
⚠ High Traffic Detected from 150.171.22.12
```

---

## Project Structure

```
Advanced-Network-Traffic-Analyzer
│
├── backend
│   ├── packet_capture.py
│   ├── api_server.py
│   └── templates
│       └── index.html
│
├── database
│   └── traffic.db
│
├── reports
│
└── README.md
```

---

## Installation

Clone the repository:

```
git clone https://github.com/YOUR_USERNAME/Advanced-Network-Traffic-Analyzer.git
```

Navigate to the project directory:

```
cd Advanced-Network-Traffic-Analyzer
```

Install required dependencies:

```
pip install scapy flask
```

---

## Usage

Start packet capture:

```
python backend/packet_capture.py
```

Start the API server:

```
python backend/api_server.py
```

Open the dashboard in your browser:

```
http://127.0.0.1:5000
```

---

## API Endpoints

Traffic data:

```
/api/traffic
```

Protocol statistics:

```
/api/protocols
```

Top source IPs:

```
/api/top_ips
```

Security alerts:

```
/api/alerts
```

---

## Example Security Alerts

```
⚠ High Traffic Detected from 192.168.1.34
⚠ High Traffic Detected from 150.171.22.12
```

These alerts are triggered when abnormal network activity is detected.

---

## Learning Outcomes

This project demonstrates:

- Network packet analysis  
- Traffic monitoring techniques  
- Intrusion detection basics  
- Backend API development  
- Real-time data visualization  
- Security monitoring concepts  

It provides hands-on experience with **network security tools and monitoring systems**.

---

## Security Disclaimer

This project is intended for **educational and research purposes only**.

Do not use this tool to monitor networks without proper authorization.

Always ensure you have permission before analyzing network traffic.

---

## Author

Cybersecurity Student  
Focused on **Network Security, Threat Detection, and SOC Monitoring Systems**
