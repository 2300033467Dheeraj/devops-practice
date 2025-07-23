#!/usr/bin/env python3
import os
import time
import socket
import subprocess

def file_operations():
    with open("sample.txt", "w") as f:
        f.write("This is a test.\n")
    with open("sample.txt", "r") as f:
        print("File contents:", f.read())

def network_operations():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(5)
        s.connect(("example.com", 80))
        s.sendall(b"GET / HTTP/1.1\r\nHost: example.com\r\n\r\n")
        print("Received:", s.recv(1024).decode())
        s.close()
    except Exception as e:
        print("Network error:", e)

def run_subprocess():
    result = subprocess.run(["ls", "-l"], capture_output=True, text=True)
    print("Subprocess output:\n", result.stdout)

def main():
    print("Starting operations...")
    file_operations()
    network_operations()
    run_subprocess()
    time.sleep(1)
    os.remove("sample.txt")

if __name__ == "__main__":
    main()
    print("Operations completed.")
# This script performs file operations, network operations, and runs a subprocess.
# It also includes error handling and cleanup of created files.
# The script is designed to be run in a Python environment with access to the filesystem and network.   