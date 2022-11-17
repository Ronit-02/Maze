def encrypt(msg, key):
    l = len(key)
    encrypted_msg = ""

    for i in range(len(msg)):
        encrypted_char = ord(msg[i]) ^ ord(key[i % l])
        encrypted_msg += chr(encrypted_char)

    return encrypted_msg