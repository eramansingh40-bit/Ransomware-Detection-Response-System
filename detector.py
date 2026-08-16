Create the detector:

nano ~/malware-lab/detector.py

Add:

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

Save:

Ctrl + O
Enter
Ctrl + X
Step 6 — Start the Detector

Open Terminal 1:

cd ~/malware-lab
python3 detector.py

Expected:

[DETECTOR] Monitoring: /home/user/malware-lab/protected

Keep this terminal running.
