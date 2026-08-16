# Malware Detection & Incident Response Lab

## Overview

This project demonstrates a simple **malware detection, behavioral analysis, and incident response workflow** using a Kali Linux virtual machine.

A harmless ransomware simulator is used instead of real malware. The simulator modifies laboratory test files by adding a `.locked` extension and creates a fake ransom note.

A Python-based detector monitors the protected directory and generates alerts when suspicious file activity is detected.

### SOC Workflow

```text
Malware Simulation
       ↓
File Activity
       ↓
Detection
       ↓
Alert Generation
       ↓
Behavioral Analysis
       ↓
Evidence Collection
       ↓
Containment
       ↓
Eradication
       ↓
Recovery
       ↓
Incident Closed
```

---

## Objectives

The objectives of this laboratory are:

* Understand basic malware behavior.
* Simulate ransomware activity safely.
* Monitor suspicious file activity.
* Detect `.locked` files.
* Detect a fake ransom note.
* Generate security alerts.
* Collect investigation evidence.
* Perform basic incident response.
* Restore clean files.
* Document the incident.

---

## Safety Notice

> **This project does not use real ransomware or destructive malware.**

The simulator:

* Does not encrypt files.
* Does not delete user data.
* Does not spread across systems.
* Does not establish persistence.
* Does not steal information.
* Does not damage the operating system.

Only dummy laboratory files inside the test directory are used.

---

# Lab Environment

| Component        | Details                       |
| ---------------- | ----------------------------- |
| Operating System | Kali Linux                    |
| Environment      | Virtual Machine               |
| Language         | Python 3                      |
| Detection Method | File activity monitoring      |
| Simulation       | Harmless ransomware behavior  |
| Evidence         | Logs and file-system activity |

---

# Project Architecture

```text
                    KALI LINUX VM
                         |
                         |
                  ┌──────▼──────┐
                  │ Test Files  │
                  └──────┬──────┘
                         |
                         ▼
              ┌────────────────────┐
              │ Ransomware Simulator│
              └──────────┬─────────┘
                         |
              ┌──────────▼──────────┐
              │ Suspicious Activity │
              │                     │
              │ *.locked files      │
              │ RANSOM_NOTE.txt     │
              └──────────┬──────────┘
                         |
                         ▼
                ┌────────────────┐
                │    Detector    │
                └───────┬────────┘
                        |
                        ▼
                ┌────────────────┐
                │ Security Alert │
                └───────┬────────┘
                        |
                        ▼
                 Investigation
                        |
                        ▼
                Evidence Collection
                        |
                        ▼
                   Containment
                        |
                        ▼
                    Recovery
```

---

# Project Structure

```text
Malware-Detection-Incident-Response-Lab/
│
├── README.md
│
├── simulator/
│   └── malware_simulator.py
│
├── detector/
│   └── detector.py
│
├── evidence/
│   └── incident_evidence.txt
│
├── logs/
│   └── alerts.log
│
├── screenshots/
│
└── reports/
    └── incident-report.md
```

---

# Step 1 — Create the Laboratory

Open the Kali Linux terminal:

```bash
mkdir -p ~/malware-lab/{protected,evidence,logs}
cd ~/malware-lab
```

Verify the directories:

```bash
ls -la
```

Expected directories:

```text
protected
evidence
logs
```

### Directory Purpose

| Directory   | Purpose                                   |
| ----------- | ----------------------------------------- |
| `protected` | Contains laboratory files being monitored |
| `evidence`  | Stores investigation evidence             |
| `logs`      | Stores detection alerts                   |

---

# Step 2 — Create Test Files

Go to the protected directory:

```bash
cd ~/malware-lab/protected
```

Create ten harmless test files:

```bash
for i in {1..10}; do
    echo "Laboratory test document $i" > "document_$i.txt"
done
```

Verify:

```bash
ls -l
```

Expected:

```text
document_1.txt
document_2.txt
document_3.txt
...
document_10.txt
```

These are dummy files created only for the laboratory.

---

# Step 3 — Create the Safe Ransomware Simulator

Go to the main laboratory directory:

```bash
cd ~/malware-lab
```

Create the simulator:

```bash
nano malware_simulator.py
```

Add:

```python
from pathlib import Path
import time

TARGET = Path.home() / "malware-lab" / "protected"

print("[LAB] Starting harmless ransomware simulation")
print(f"[LAB] Target directory: {TARGET}")

files = list(TARGET.glob("*.txt"))

for file in files:
    new_name = file.with_name(file.name + ".locked")
    file.rename(new_name)

    print(
        f"[LAB] Simulated modification: "
        f"{file.name} -> {new_name.name}"
    )

    time.sleep(0.5)

note = TARGET / "RANSOM_NOTE.txt"

note.write_text(
    "THIS IS A SAFE LABORATORY SIMULATION.\n"
    "NO REAL RANSOMWARE WAS USED.\n"
)

print("[LAB] Fake ransom note created")
print("[LAB] Simulation complete")
```

Save the file:

```text
Ctrl + O
Enter
Ctrl + X
```

---

# Step 4 — Test the Simulator

Check the original files:

```bash
ls ~/malware-lab/protected
```

Run the simulator:

```bash
python3 ~/malware-lab/malware_simulator.py
```

Example output:

```text
[LAB] Starting harmless ransomware simulation
[LAB] Target directory: /home/user/malware-lab/protected
[LAB] Simulated modification: document_1.txt -> document_1.txt.locked
[LAB] Simulated modification: document_2.txt -> document_2.txt.locked
[LAB] Simulated modification: document_3.txt -> document_3.txt.locked
...
[LAB] Fake ransom note created
[LAB] Simulation complete
```

Check the directory:

```bash
ls ~/malware-lab/protected
```

Expected:

```text
document_1.txt.locked
document_2.txt.locked
document_3.txt.locked
...
RANSOM_NOTE.txt
```

---

# Step 5 — Create the Malware Detector

Create the detector:

```bash
nano ~/malware-lab/detector.py
```

Add:

```python
from pathlib import Path
import time

TARGET = Path.home() / "malware-lab" / "protected"
LOG = Path.home() / "malware-lab" / "logs" / "alerts.log"

print("[DETECTOR] Monitoring:", TARGET)

previous = set(TARGET.iterdir())

while True:

    current = set(TARGET.iterdir())

    new_files = current - previous

    for file in new_files:

        if file.name.endswith(".locked"):

            alert = (
                f"[HIGH] Suspicious ransomware indicator detected: "
                f"{file.name}"
            )

            print(alert)

            with open(LOG, "a") as log:
                log.write(alert + "\n")

        elif file.name == "RANSOM_NOTE.txt":

            alert = "[CRITICAL] Ransom note detected"

            print(alert)

            with open(LOG, "a") as log:
                log.write(alert + "\n")

    previous = current

    time.sleep(1)
```

Save:

```text
Ctrl + O
Enter
Ctrl + X
```

---

# Step 6 — Start the Detector

Open Terminal 1:

```bash
cd ~/malware-lab
python3 detector.py
```

Expected:

```text
[DETECTOR] Monitoring: /home/user/malware-lab/protected
```

Keep this terminal running.

---

# Step 7 — Reset the Laboratory

Open Terminal 2:

```bash
cd ~/malware-lab/protected
```

Remove previous simulated files:

```bash
rm -f *.locked RANSOM_NOTE.txt
```

Recreate the clean test files:

```bash
for i in {1..10}; do
    echo "Laboratory test document $i" > "document_$i.txt"
done
```

---

# Step 8 — Run the Malware Simulation

Keep the detector running in Terminal 1.

From Terminal 2:

```bash
python3 ~/malware-lab/malware_simulator.py
```

The detector should now generate alerts.

Example:

```text
[HIGH] Suspicious ransomware indicator detected: document_1.txt.locked
[HIGH] Suspicious ransomware indicator detected: document_2.txt.locked
[HIGH] Suspicious ransomware indicator detected: document_3.txt.locked
[HIGH] Suspicious ransomware indicator detected: document_4.txt.locked
[CRITICAL] Ransom note detected
```

This demonstrates the **malware detection stage**.

---

# Step 9 — Review Security Alerts

Run:

```bash
cat ~/malware-lab/logs/alerts.log
```

Example:

```text
[HIGH] Suspicious ransomware indicator detected: document_1.txt.locked
[HIGH] Suspicious ransomware indicator detected: document_2.txt.locked
[HIGH] Suspicious ransomware indicator detected: document_3.txt.locked
[CRITICAL] Ransom note detected
```

The alert log provides evidence that suspicious activity was detected.

---

# Step 10 — Behavioral Malware Analysis

This project performs **behavioral analysis** rather than reverse engineering.

### Observed Behavior

The simulator caused files to change from:

```text
document_1.txt
```

to:

```text
document_1.txt.locked
```

A fake ransom note was also created:

```text
RANSOM_NOTE.txt
```

### Indicators

| Indicator      | Observation                 |
| -------------- | --------------------------- |
| File extension | `.locked`                   |
| Ransom note    | `RANSOM_NOTE.txt`           |
| Activity       | Multiple file modifications |
| Target         | `~/malware-lab/protected/`  |
| Process        | `malware_simulator.py`      |

### Analysis Conclusion

The observed behavior is consistent with a ransomware-like file modification pattern, but the activity was generated by a controlled laboratory simulator.

---

# Step 11 — Collect Evidence

Create an evidence snapshot:

```bash
cd ~/malware-lab
```

```bash
{
    echo "===== DATE ====="
    date

    echo
    echo "===== PROTECTED DIRECTORY ====="
    ls -lah protected

    echo
    echo "===== ALERT LOG ====="
    cat logs/alerts.log

    echo
    echo "===== PROCESSES ====="
    ps aux

} > evidence/incident_evidence.txt
```

Review the evidence:

```bash
cat evidence/incident_evidence.txt
```

---

# Step 12 — Incident Response

The incident-response process used in this laboratory is:

```text
DETECT
   ↓
VALIDATE
   ↓
CONTAIN
   ↓
COLLECT EVIDENCE
   ↓
ERADICATE
   ↓
RECOVER
   ↓
LESSON LEARNED
```

## Detection

The detector identified:

* `.locked` files
* Fake ransom note
* Multiple suspicious file modifications

## Validation

The activity was investigated and confirmed to be generated by the laboratory simulator.

## Containment

Stop the detector:

```text
Ctrl + C
```

Create an evidence directory:

```bash
mkdir -p ~/malware-lab/evidence/suspicious_files
```

Move suspicious files:

```bash
mv ~/malware-lab/protected/*.locked \
~/malware-lab/evidence/suspicious_files/
```

Move the fake ransom note:

```bash
mv ~/malware-lab/protected/RANSOM_NOTE.txt \
~/malware-lab/evidence/suspicious_files/
```

## Eradication

Remove or preserve the simulator according to the laboratory objective.

For evidence preservation, it can be moved into the evidence directory rather than immediately deleted.

## Recovery

Recreate clean laboratory files:

```bash
cd ~/malware-lab/protected

for i in {1..10}; do
    echo "Clean laboratory document $i" > "document_$i.txt"
done
```

Verify:

```bash
ls -lah
```

The protected directory should now contain clean laboratory files.

---

# Incident Summary

| Field              | Value                         |
| ------------------ | ----------------------------- |
| Incident ID        | INC-001                       |
| Incident Type      | Ransomware Simulation         |
| Severity           | High                          |
| Host               | Kali Linux VM                 |
| Detection          | `.locked` files + ransom note |
| Affected Directory | `~/malware-lab/protected`     |
| Initial Indicator  | Multiple file modifications   |
| Analysis           | Behavioral Analysis           |
| Containment        | Suspicious files isolated     |
| Evidence           | `incident_evidence.txt`       |
| Recovery           | Clean test files restored     |
| Malware            | Harmless simulator            |
| Status             | Resolved                      |

---

# Evidence

Recommended screenshots for the GitHub repository:

### 1. Laboratory Directory

```text
screenshots/01-lab-directory.png
```

Shows:

```bash
ls -la ~/malware-lab
```

### 2. Original Test Files

```text
screenshots/02-test-files.png
```

Shows:

```text
document_1.txt
document_2.txt
...
document_10.txt
```

### 3. Simulation

```text
screenshots/03-malware-simulation.png
```

Shows the simulator running.

### 4. Detection

```text
screenshots/04-detection-alert.png
```

Shows:

```text
[HIGH] Suspicious ransomware indicator detected
[CRITICAL] Ransom note detected
```

### 5. Alert Log

```text
screenshots/05-alert-log.png
```

Shows:

```bash
cat ~/malware-lab/logs/alerts.log
```

### 6. Incident Response

```text
screenshots/06-incident-response.png
```

Shows suspicious files being isolated and clean files being restored.

---

# MITRE ATT&CK Mapping

This laboratory demonstrates ransomware-like behavior at a simplified level.

| Technique                    | ID    | Relevance                                                                       |
| ---------------------------- | ----- | ------------------------------------------------------------------------------- |
| Data Encrypted for Impact    | T1486 | Simulated ransomware behavior; files are renamed rather than actually encrypted |
| File and Directory Discovery | T1083 | Simulator identifies files in the protected directory                           |

> This is a simplified educational mapping. The simulator does not perform real encryption.

---

# Key Skills Demonstrated

This project demonstrates:

* Linux command-line skills
* Python scripting
* File-system monitoring
* Malware behavioral analysis
* Security alert generation
* Evidence collection
* Incident investigation
* Incident containment
* Recovery procedures
* Basic MITRE ATT&CK mapping
* SOC incident-response workflow

---

# Final Result

The laboratory demonstrates the complete security workflow:

```text
        SAFE SIMULATION
              ↓
       SUSPICIOUS ACTIVITY
              ↓
          DETECTION
              ↓
            ALERT
              ↓
        INVESTIGATION
              ↓
      EVIDENCE COLLECTION
              ↓
         CONTAINMENT
              ↓
         ERADICATION
              ↓
           RECOVERY
              ↓
       INCIDENT CLOSED
```

---

# Disclaimer

This project is intended for **educational and defensive cybersecurity training only**.

No real ransomware or destructive malware is used. All file modifications occur inside a controlled Kali Linux laboratory environment using dummy files.
