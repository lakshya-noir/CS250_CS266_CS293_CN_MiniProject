# 🔍 Network Fingerprinting & Analysis Tool

A modular Python-based tool for performing basic network fingerprinting and server analysis using banner grabbing, latency measurement, and SSL/TLS inspection.

This project demonstrates how publicly exposed server information can be collected and analyzed using low-level networking concepts.

---

## 🚀 Key Features

- 🌐 DNS Resolution  
  Converts domain names into IP addresses  

- ⚡ Latency Measurement  
  Calculates round-trip time to target servers  

- 📡 Banner Grabbing  
  Extracts HTTP response headers from servers  

- 🧠 Server Identification  
  Infers server type (Apache, Nginx, IIS, etc.)  

- 🔐 SSL/TLS Inspection  
  Retrieves certificate details, TLS version, and cipher suite  

- 📊 Data Visualization  
  Generates graphs for accuracy and performance analysis  

---

## 📁 Project Structure

```
.
├── main.py                      # Entry point — orchestrates the full fingerprinting pipeline
│
├── core/
│   ├── scanner.py               # Main fingerprinting pipeline
│   ├── banner.py                # Banner grabbing logic
│   ├── identifier.py            # Server identification logic
│   ├── ssl_analyzer.py          # SSL/TLS inspection
│
├── utils/
│   └── utils.py                 # Utility functions
│
├── visualization/
│   ├── accuracy_vs_servers.py   # Accuracy graph generation
│   └── servers_vs_scantime.py   # Performance graph generation
│
├── Graphs/
│   └── accuracy_vs_servers.png  # Generated graph 1
│   └── servers_vs_scantime.png  # Generated graph 2
│
└── requirements.txt             # Python dependencies
```
## ⚙️ How It Works

Pipeline:

Target → Resolve → Connect → Measure → Analyze → Report

Step-by-step:

1. Resolve hostname to IP  
2. Measure latency  
3. Grab HTTP banner  
4. Identify server type  
5. Extract SSL details (if HTTPS)  
6. Generate output + graphs  

---

## ▶️ How to Run

### 1. Install dependencies

```pip install -r requirements.txt``` 

### 2. Run the tool

```python main.py``` 

---

## 🎯 Example Targets

Defined inside main.py:

python targets = [     ("google.com", 443),     ("example.com", 80),     ("github.com", 443), ] 

You can modify or extend this list.

---

## 🧪 Sample Output

```
Target : github.com
Port   : 443
IP     : 140.82.x.x
Latency: 18.2 ms

--- Banner ---
HTTP/1.1 200 OK
Server: GitHub.com

--- Identified Server ---
GitHub Infrastructure

--- SSL Info ---
TLS Version : TLSv1.3
Cipher      : TLS_AES_128_GCM_SHA256
Issuer      : DigiCert
```

---

## 📊 Output Graphs

Generated in the outputs/ directory:

- accuracy_vs_servers.png  
  Shows how identification accuracy changes with scale  

- servers_vs_scantime.png  
  Shows how scan time increases with number of targets  

---

## 📚 Concepts Covered

- Socket Programming (TCP)  
- DNS Resolution  
- HTTP Protocol (Headers, Requests)  
- SSL/TLS Handshake Basics  
- Network Latency Measurement  
- Basic Fingerprinting Techniques  

---

## 🧠 What This Project Demonstrates

- Understanding of client-server interaction  
- Practical use of networking protocols  
- Awareness of security exposure through banners  
- Ability to design modular Python systems  

---
