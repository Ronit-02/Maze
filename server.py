import socket

# host ip and port
SERVER_IP = '192.168.1.4'  
PORT = 5678

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((SERVER_IP, PORT))
    s.listen(1)

    conn, addr = s.accept()
    with conn:
        while True:
            data = conn.recv(1024)
            print(data)
            