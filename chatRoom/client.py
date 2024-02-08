import socket
import threading

def receive_messages(sock):
    while True:
        msg = sock.recv(1024).decode('utf-8')
        print(f'Received from {msg}')

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('5.tcp.eu.ngrok.io', 16755))#u ovom formatu treba ngrok
#client.connect(('localhost', 12345))#za hosta

receive_handler = threading.Thread(target=receive_messages, args=(client,))
receive_handler.start()

while True:
    msg = input('')
    client.send(msg.encode('utf-8'))
