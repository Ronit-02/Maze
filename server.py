import socket

# host ip and port
SERVER_IP = 'localhost'  
SERVER_PORT = 5678
FORMAT = 'utf-8'

# TCP IPv4 socket
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:

    # bind
    s.bind((SERVER_IP, SERVER_PORT))
    print('Listening....')

    # listen
    s.listen(1)

    # connect
    conn, addr = s.accept()
    print('connection established with ',addr)

    with conn:
        while True:
            # send
            conn.send('Send me bitcoins!'.encode(FORMAT))

            # receive
            data = conn.recv(1024).decode(FORMAT)
            print(data)