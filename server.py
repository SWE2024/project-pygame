import threading
import socket
import platform
import subprocess

server = None

def get_private_ip():
    system = platform.system()
    if system == "Windows":
        address = socket.gethostbyname(socket.gethostname())
    elif system == "Linux":
        address = subprocess.run(['hostname', '-I'], capture_output=True).stdout.decode('utf-8').strip()
    elif system == "Darwin":
        command1 = ["ifconfig" ,"en0"]
        process1 = subprocess.Popen(command1, stdout=subprocess.PIPE)
        process1.wait()
        output = process1. communicate()[0].decode('utf-8')
        process1.stdout.close()

        index = output.find('inet ') + len('inet ')
        output = output[index:].split(' ')
        address = output[0]
        
    return address

def start():
    server.listen()
    print(f'[Listening] Server is listening on {server.getsockname()}')
    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()
        print(f'[active connections] {threading.active_count() - 1}')

def handle_client(conn, addr):
    print(f'[New Connection] {addr} connected')
    connected = True
    while connected:

        msg_length = conn.recv(64).decode('utf-8')
        if msg_length:
            msg = conn.recv(int(msg_length)).decode('utf-8')

            if msg == "!disconnect":
                connected = False

            print(f'[{addr}] {msg}')

    conn.close()

if __name__ == "__main__":
    print(get_private_ip())
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((get_private_ip(), 5050))
    start()