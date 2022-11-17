# Decrypt Function
def decrypt(msg, key):
    l = len(key)
    decrypted_msg = ""

    for i in range(len(msg)):
        decrypted_char = ord(msg[i]) ^ ord(key[i % l])
        decrypted_msg += chr(decrypted_char)

    return decrypted_msg