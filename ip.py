import platform
import socket
import subprocess

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

ip = '127.0.0.1'
# ip = get_private_ip()

port = 12345


