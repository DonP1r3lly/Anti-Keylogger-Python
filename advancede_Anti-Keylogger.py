# Basic Anti-Keylogger
# June 2024
# GitHub (DonP1r3lly)

import psutil
import os
import signal


def detect_python_processes():
    print("Detecting running Python Processes...\n")

    for proc in psutil.process_iter(['pid', 'name']):
        if 'python' in proc.info['name']:
            print(f"PID: {proc.info['pid']}, Process Name: {proc.info['name']}")

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

def main():
    while True:
        print("\nSelect an option:")
        print("1. Detect running Python processes")
        print("2. Kill a process by PID")
        print("3. Exit")

        option = input("Enter your choice (1/2/3): ")

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
            print("The program was Finished.")
            break
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")

if __name__ == "__main__":
    main()