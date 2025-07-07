# Auto Vuln Tracker for Kali Linux

A simple tool to **automate vulnerability scans, log results, and generate graphs** while practicing pentesting on Kali Linux.

---

## 🛠️ Features

✅ Runs `nmap` with vuln scripts on any target IP.  
✅ Automatically saves the scan to a folder with the machine's name.  
✅ Logs the number of potential vulnerabilities found in a CSV file.  
✅ Generates a graph to visualize your scanning progress over time.  
✅ Helps you organize your HackTheBox or lab practice in a structured way.

---

## 🚩 Requirements

- **Kali Linux** or any Linux with:
  - `bash`
  - `nmap`
  - `python3`
  - Python `matplotlib`

To install `matplotlib` if not installed:
```bash
sudo apt update
sudo apt install python3-pip -y
pip3 install matplotlib
```

---

## 📦 Installation

1️⃣ Clone your repository:
```bash
git clone https://github.com/<your_username>/Auto-Vuln-Tracker.git
```
2️⃣ Move scripts to your working folder:
```bash
mkdir -p ~/VulnTracker
mv Auto-Vuln-Tracker/auto_vuln_tracker.sh ~/VulnTracker/
mv Auto-Vuln-Tracker/generate_vuln_graph.py ~/VulnTracker/
```
3️⃣ Make scripts executable:
```bash
chmod +x ~/VulnTracker/auto_vuln_tracker.sh
chmod +x ~/VulnTracker/generate_vuln_graph.py
```

---

## 🚀 Usage

After you finish enumerating a machine or want to check vulnerabilities:

### Run the scanner:
```bash
cd ~/VulnTracker
./auto_vuln_tracker.sh <IP> <MachineName>
```
**Example:**
```bash
./auto_vuln_tracker.sh 10.10.10.10 Arctic
```

This will:
✅ Run `nmap` with vuln scripts on the target IP.  
✅ Save results in:
```
~/VulnTracker/<MachineName>/nmap_vuln_scan.txt
```
✅ Log results in:
```
~/VulnTracker/vuln_log.csv
```
✅ Generate/Update your graph:
```
~/VulnTracker/vuln_summary.png
```

---

### View your graph:
To open the graph:
```bash
xdg-open ~/VulnTracker/vuln_summary.png
```

---

## 🗂️ Folder Structure

- `~/VulnTracker/<MachineName>/` : Stores each scan.
- `~/VulnTracker/vuln_log.csv` : Stores your vulnerability scan history.
- `~/VulnTracker/vuln_summary.png` : Visual summary of your progress.

---

## 📜 License

MIT License

---

## 🤝 Contributing

This is for personal practice while learning pentesting. Feel free to fork and modify it to fit your workflow.

---

**✨ Track your pentesting learning with real data, visualize your progress, and keep your practice organized.**
