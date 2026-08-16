# Incident Report — Ransomware Simulation

# Incident Overview

# Field	Details
Incident ID	INC-001
Incident Type	Ransomware Simulation
Severity	High
Status	Resolved
Host	Kali Linux VM
Environment	Controlled Cybersecurity Laboratory
Detection Method	Python File Activity Detector
Analysis Type	Behavioral Analysis
Affected Directory	~/malware-lab/protected
Initial Indicator	Multiple .locked files
Secondary Indicator	RANSOM_NOTE.txt
Malware Type	Harmless Ransomware Simulator


# Executive Summary

This incident was generated as part of a controlled malware detection and incident-response laboratory.

A harmless ransomware simulator was executed inside a Kali Linux virtual machine. The simulator operated only on dummy laboratory files located in:

~/malware-lab/protected

The simulator renamed test files by adding the .locked extension and created a fake ransom note named:

RANSOM_NOTE.txt

A Python-based detection script continuously monitored the protected directory. When suspicious files appeared, the detector generated security alerts and recorded them in:

~/malware-lab/logs/alerts.log

The activity was then investigated using behavioral analysis. Evidence was collected, suspicious files were isolated, and clean laboratory files were restored.

No real ransomware, destructive malware, data theft, persistence, or system damage was involved.
