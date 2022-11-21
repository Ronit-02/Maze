import socket

# host ip and port
SERVER_IP = '192.168.1.8'  
SERVER_PORT = 5678

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((SERVER_IP, SERVER_PORT))
    print('Listening....')
    s.listen(1)
    print('naman1')

    conn, addr = s.accept()
    print('naman2')
    print(f'connection established : {addr}')
    with conn:
        while True:
            data = conn.recv(1024)
            print(data)
            # s.send('Send me bitcoins!'.encode('utf-8'))
            break