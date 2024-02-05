import threading
import socket
import platform
import subprocess

server = None

def get_private_ip():
    system = platform.system()
    if system == "Windows":
        command = []
    elif system == "Linux":
        command = ['hostname', '-I']
    elif system == "Darwin":
        command = []

    address = subprocess.run(command, capture_output=True).stdout.decode('utf-8').strip()
    return address

def start():
    server.listen()
    print(f'[Listening] Server is listening on {get_private_ip()}')
    while True:
        try:
            pass
        except KeyboardInterrupt:
            print("server shutting down")
            server.close()
            quit()

        conn, addr = server.accept()
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()
        print(f'[active connections] {threading.active_count() - 1}')

def handle_client(conn, addr):
    print(f'[New Connection] {addr} connected')
    connected = True
    while connected:
        try:
            pass
        except KeyboardInterrupt:
            print("server shutting down")
            conn.close()
            server.close()
            quit()

        msg_length = conn.recv(64).decode('utf-8')
        if msg_length:
            msg = conn.recv(int(msg_length)).decode('utf-8')

            if msg == "!disconnect":
                connected = False

            print(f'[{addr}] {msg}')

    conn.close()

if __name__ == "__main__":
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((get_private_ip(), 5050))
    start()