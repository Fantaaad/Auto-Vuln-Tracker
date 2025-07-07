# Auto Vuln Tracker for Kali Linux

**Auto Vuln Tracker** is a simple tool to **automate vulnerability scanning, logging, and progress visualization** while practicing pentesting on **Kali Linux**.

It helps you track your learning, organize your HackTheBox or lab practice, and visually measure your progress while learning vulnerability detection.

---

## ✨ Features

✅ Runs `nmap` with vulnerability scripts against a target IP automatically.  
✅ Saves scans in a folder named after the machine.  
✅ Logs the number of potential vulnerabilities in a CSV file.  
✅ Generates a visual graph showing vulnerabilities found across machines.  
✅ Keeps your pentesting practice organized and structured.

---

## 🚩 Requirements

- **Kali Linux** or any Linux with:
  - `bash`
  - `nmap`
  - `python3`
  - Python library: `matplotlib`

**Install dependencies if needed:**
```bash
sudo apt update
sudo apt install nmap python3 python3-pip -y
pip3 install matplotlib
```

---

## 📦 Installation

1️⃣ Clone your repository:
```bash
git clone https://github.com/Fantaaad/Auto-Vuln-Tracker.git
```

2️⃣ Move into your working directory:
```bash
cd Auto-Vuln-Tracker
```

3️⃣ Make scripts executable:
```bash
chmod +x auto_vuln_tracker.sh
chmod +x generate_vuln_graph.py
```

---

## 🚀 Usage

After you complete or want to scan a machine:

### ✅ **Run the vulnerability tracker:**
```bash
./auto_vuln_tracker.sh <IP> <MachineName>
```
**Example:**
```bash
./auto_vuln_tracker.sh 10.10.10.10 Arctic
```

This will:
✅ Run `nmap` with vuln scripts on the specified IP.  
✅ Save results in:
```
~/VulnTracker/<MachineName>/nmap_vuln_scan.txt
```
✅ Log the machine, IP, vulnerabilities found, and date into:
```
~/VulnTracker/vuln_log.csv
```
✅ Generate or update your visual summary:
```
~/VulnTracker/vuln_summary.png
```

---

### ✅ **View your vulnerability progress graph:**
```bash
xdg-open ~/VulnTracker/vuln_summary.png
```

---

## 🗂️ Folder Structure

- `~/VulnTracker/<MachineName>/` - Contains individual scans and reports.
- `~/VulnTracker/vuln_log.csv` - Tracks your scans and detected vulnerabilities.
- `~/VulnTracker/vuln_summary.png` - Shows your progress visually.

---

## 📜 License

MIT License

---

## 🤝 Contributing

This project is for personal pentesting practice and workflow structuring while learning. Feel free to fork and adapt it to your workflow or learning goals.

---

**✨ Organize your pentesting practice while visualizing your growth, automating your scans, and building a real workflow on Kali Linux.**
