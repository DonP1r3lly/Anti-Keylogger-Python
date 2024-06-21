# Basic Anti-Keylogger
# June 2024
# GitHub (DonP1r3lly)

import psutil

def detect_python_processes():
    print("Detecting running Python Processes...\n")

    for proc in psutil.process_iter(['pid', "name"]):
        if 'python' in proc.info['name']:
            print(f"PID: {proc.info['pid']}, Process Name: {proc.info['name']}")

if __name__=="__main__":
    detect_python_processes()