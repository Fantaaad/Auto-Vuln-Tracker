#!/bin/bash

# Auto Vuln Tracker for Kali Linux
# Usage: ./auto_vuln_tracker.sh <IP> <MachineName>
# Example: ./auto_vuln_tracker.sh 10.10.10.10 Arctic

if [ "$#" -ne 2 ]; then
    echo "Usage: $0 <IP> <MachineName>"
    exit 1
fi

IP=$1
NAME=$2
DATE=$(date +%Y-%m-%d)

BASE_DIR=~/VulnTracker/$NAME
mkdir -p "$BASE_DIR"

# Run nmap vuln scan
echo "[+] Running Nmap vuln scan against $IP..."
nmap -sV --script vuln -oN "$BASE_DIR/nmap_vuln_scan.txt" "$IP"

echo "[+] Parsing vulnerabilities found..."
VULNS=$(grep 'VULNERABLE:' "$BASE_DIR/nmap_vuln_scan.txt" | wc -l)

# Update CSV log
CSV=~/VulnTracker/vuln_log.csv
if [ ! -f "$CSV" ]; then
    echo "Machine,IP,PossibleVulns,Date" > "$CSV"
fi
echo "$NAME,$IP,$VULNS,$DATE" >> "$CSV"
echo "[+] Logged $VULNS possible vulnerabilities in $CSV"

# Generate updated graph
~/VulnTracker/generate_vuln_graph.py

echo "[+] Scan and log complete for $NAME."

