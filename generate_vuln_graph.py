#!/usr/bin/env python3

import csv
import matplotlib.pyplot as plt
from collections import Counter
import os
from datetime import datetime

# Paths
csv_file = os.path.expanduser('~/VulnTracker/vuln_log.csv')
output_file = os.path.expanduser('~/VulnTracker/vuln_summary.png')

# Check if CSV exists
if not os.path.exists(csv_file):
    print("[!] No vuln_log.csv found. Run auto_vuln_tracker.sh first.")
    exit()

# Parse CSV
machines = []
vuln_counts = []
dates = []

with open(csv_file, 'r') as file:
    reader = csv.DictReader(file)
    for row in reader:
        machines.append(row['Machine'])
        vuln_counts.append(int(row['PossibleVulns']))
        dates.append(datetime.strptime(row['Date'], '%Y-%m-%d'))

# Count total vulns per machine
vuln_summary = Counter()
for m, v in zip(machines, vuln_counts):
    vuln_summary[m] += v

# Prepare data for plotting
labels = list(vuln_summary.keys())
values = list(vuln_summary.values())

# Plot
plt.figure(figsize=(10, 6))
plt.bar(labels, values)
plt.xlabel('Machine')
plt.ylabel('Possible Vulnerabilities Found')
plt.title('Vulnerabilities Detected per Machine')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.savefig(output_file)
plt.close()

print(f"[+] Graph generated at {output_file}")
