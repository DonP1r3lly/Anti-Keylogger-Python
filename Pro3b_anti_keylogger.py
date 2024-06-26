# Pro Anti-Keylogger
# June 2024
# GitHub (DonP1r3lly)

import psutil
import os
import signal
import json


def detect_python_processes():
    print("Detecting running Python Processes...\n")

    python_processes = []
    for proc in psutil.process_iter(['pid', 'name', 'cmdline']):
        try:
            if 'python' in proc.info['name'].lower():  
                cmdline = proc.info['cmdline']
                if cmdline and len(cmdline) > 1:  
                    script = cmdline[1]  
                    if script.endswith('.py'):
                        python_processes.append(proc)
                        print(f"PID: {proc.info['pid']}, Process Name: {proc.info['name']}, Script: {script}")
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass

    return python_processes


def kill_process(pid):
    print(f"Attempting to kill process with PID: {pid}...")
    try:
        os.kill(pid, signal.SIGTERM)
        print(f"Process with PID: {pid} has been terminated.")
    except ProcessLookupError:
        print(f"No running process with PID: {pid}.")
    except PermissionError:
        print(f"Permission denied to kill process with PID: {pid}.")
    except OSError as e:
        print(f"Error: {e}. The PID {pid} might not be valid on this system.")


def search_ioc():
    try:
        with open("Pro3_IOC.json") as file:
            IOCs = json.load(file)

        print("List de IOC:")
        for ioc in IOCs["process_name"]:
            print(ioc)
        for script in IOCs["script_name"]:
            print(script)

        processes = detect_python_processes()
        found = False

        print("\nScanning running processes...")
        for proc in processes:
            proc_name = proc.info['name']
            cmdline = proc.info['cmdline']
            if proc_name in IOCs["process_name"]:
                print(f"A running IOC process was found: {proc_name} with PID {proc.info['pid']}")
                found = True
            else:
                for script in IOCs["script_name"]:
                    if any(script in s for s in cmdline):
                        print(f"A running IOC process was found: {script} in process {proc_name} with PID {proc.info['pid']}")
                        found = True

        if not found:
            print("No running IOC processes found.")
    except FileNotFoundError:
        print("Error: Pro3_IOC.json NO Found.")

def main():
    while True:
        print("\nSelect an option:")
        print("1. Detect running Python processes")
        print("2. Kill a process by PID")
        print("3. Search IOC")
        print("4. Exit")
        print("5. This code was made by DonP1r3lly (GitHub)")

        option = input("Enter your choice (1/2/3/4): ")

        if option == '1':
            detect_python_processes()
        elif option == '2':
            while True:
                try:
                    pid = int(input("Enter the PID of the process to kill: "))
                    kill_process(pid)
                    print("The process was finished")
                    break  
                except ValueError:
                    print("Invalid PID. Please enter a numeric value.")
                except OSError as e:
                    print(f"Error: {e}. The PID {pid} might not be valid on this system.")
        elif option == '3':
            print("IOC list will be checked")
            search_ioc()
        elif option == '4':
            print("The program was Finished.")
            break
        else:
            print("Invalid choice. Please enter 1, 2, 3 or 4.")

if __name__ == "__main__":
    main()
