import socket
from server import get_private_ip

def send(msg):
    message = msg.encode('utf-8')
    send_length = str(len(message)).encode('utf-8')
    send_length += b' ' * (64 - len(send_length))

    client.send(send_length)
    client.send(message)



ip = "10.2.120.58"
# ip = get_private_ip()
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((ip, 5050))


while True:
    try:
        userinput = input(">>>\t")
    except KeyboardInterrupt:
        print('\nchat closed')
        send("!disconnect")
        quit()

    
    send(userinput)


