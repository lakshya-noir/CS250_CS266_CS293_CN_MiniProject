# 🔍 Network Fingerprinting & Analysis Tool

A modular Python-based tool for performing basic network fingerprinting and server analysis using banner grabbing, latency measurement, and SSL/TLS inspection.

This project demonstrates how publicly exposed server information can be collected and analyzed using low-level networking concepts.

---

## 🚀 Key Features

- 🌐 DNS Resolution
  - Converts domain names into IP addresses

- ⚡ Latency Measurement
  - Calculates round-trip time to target servers

- 📡 Banner Grabbing
  - Extracts HTTP response headers from servers

- 🧠 Server Identification
  - Infers server type (Apache, Nginx, IIS, etc.)

- 🔐 SSL/TLS Inspection
  - Retrieves certificate details
  - Displays TLS version and cipher suite

- 📊 Data Visualization
  - Graphs for:
    - Accuracy vs number of servers
    - Performance vs number of requests

---

## 🧱 Project Structure

bash . ├── main.py                  # Entry point ├── core/ │   ├── scanner.py          # Main fingerprinting pipeline │   ├── banner.py           # Banner grabbing logic │   ├── identifier.py       # Server identification logic │   ├── ssl_analyzer.py     # SSL/TLS inspection │   └── latency.py          # Latency measurement │ ├── utils/ │   ├── resolver.py         # DNS resolution │   └── helpers.py          # Utility functions │ ├── visualization/ │   ├── accuracy_plot.py    # Accuracy graph │   └── performance_plot.py # Performance graph │ ├── requirements.txt └── outputs/     ├── *.png               # Generated graphs 

---

## ⚙️ How It Works

The tool follows a structured pipeline:

text Target → Resolve → Connect → Measure → Analyze → Report 

### Step-by-step Flow

1. Resolve hostname → IP
2. Measure latency
3. Grab HTTP banner
4. Identify server type
5. Extract SSL details (if HTTPS)
6. Store + visualize results

---

## ▶️ How to Run

### 1. Install dependencies

bash pip install -r requirements.txt 

### 2. Run the tool

bash python main.py 

---

## 🎯 Example Targets

Defined inside main.py:

python targets = [     ("google.com", 443),     ("example.com", 80),     ("github.com", 443), ] 

You can modify or extend this list.

---

## 🧪 Sample Output

text ============================================================ Target: github.com Port: 443 IP: 140.82.x.x Latency: 18.2 ms  --- Banner --- HTTP/1.1 200 OK Server: GitHub.com  --- Identified Server --- GitHub Infrastructure  --- SSL Info --- TLS Version: TLSv1.3 Cipher: TLS_AES_128_GCM_SHA256 Issuer: DigiCert ============================================================ 

---

## 📊 Output Graphs

Generated in the outputs/ directory:

- accuracy_vs_servers.png
  - Shows how identification accuracy changes with scale

- performance_vs_targets.png
  - Shows latency trends as targets increase

---

## 📚 Concepts Covered

- Socket Programming (TCP)
- DNS Resolution
- HTTP Protocol (Headers, Requests)
- SSL/TLS Handshake Basics
- Network Latency Measurement
- Basic Fingerprinting Techniques

---

## ⚠️ Limitations (Be Honest in Viva)

- Detection is heuristic-based (string matching)
- Cannot bypass:
  - CDNs (Cloudflare, Akamai)
  - Hidden server headers
- No deep packet inspection
- Sequential execution (no concurrency)

---

## 🔧 Suggested Improvements

If you want to stand out:

- Add multithreading / asyncio
- Implement port scanning
- Use regex-based detection
- Add logging system
- Build a simple CLI interface
- Export results as JSON/CSV

---

## 🧠 What This Project Shows

- Understanding of how clients interact with servers
- Practical use of networking protocols
- Awareness of security exposure via banners
- Ability to design modular Python systems

---

## 👨‍💻 Author

Computer Networks Mini Project  
Built for academic demonstration and learning

---

## ⚠️ Disclaimer

This tool is intended for educational purposes only.  
Do not scan or probe systems without proper authorization.
