#!/usr/bin/env python

import platform
import os
import subprocess

def change_hostname(new_hostname):
    system_platform = platform.system()
    
    if system_platform == "Darwin":  # macOS
        subprocess.run(["sudo", "scutil", "--set", "ComputerName", new_hostname])
        subprocess.run(["sudo", "scutil", "--set", "HostName", new_hostname])
        subprocess.run(["sudo", "scutil", "--set", "LocalHostName", new_hostname])
    
    elif system_platform == "Linux":
        # Update the /etc/hostname file
        with open("/etc/hostname", "w") as hostname_file:
            hostname_file.write(new_hostname)
        
        # Change the current hostname
        subprocess.run(["sudo", "hostnamectl", "set-hostname", new_hostname])
    
    elif system_platform == "Windows":
        # Changing hostname on Windows is more complex and requires registry changes.
        # Here's a basic example using PowerShell:
        powershell_command = f"Rename-Computer -NewName {new_hostname} -Force -Restart"
        subprocess.run(["powershell", "-Command", powershell_command], shell=True)
    
    else:
        print("Unsupported platform. This script supports macOS, Linux, and Windows.")

if __name__ == "__main__":
    new_hostname = "YourNewHostname"  # Replace with your desired hostname
    change_hostname(new_hostname)
