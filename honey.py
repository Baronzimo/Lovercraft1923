import socket
import re

def handle_connection(client_socket, client_address):
    print("Connection received from:", client_address)

    response = b"SSH-2.0-OpenSSH_7.4p1 Debian-10+deb9u7\r\n"

    try:
        client_socket.sendall(response)

        data = client_socket.recv(1024)
        if b'SSH_MSG_USERAUTH_REQUEST' in data:
            data_str = data.decode('latin-1')
            match = re.search(rb'user (.+?)\x00', data)
            if match:
                username = match.group(1).decode('latin-1')
                print("Username:", username)

        print("Received data (raw bytes):", data)
        print("Received data (decoded):", data.decode('latin-1'))

    except ConnectionResetError:
        print("Connection reset by peer.")

    client_socket.close()

def start_honeypot():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_socket.bind(('0.0.0.0', 22))
    server_socket.listen(5)

    print("Honeypot started. Listening for connections...")

    while True:
        client_socket, client_address = server_socket.accept()
        handle_connection(client_socket, client_address[0])

if __name__ == '__main__':
    start_honeypot()
