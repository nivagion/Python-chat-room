import socket
import threading

def handle_client(client_socket, client_number):
    while True:
        msg = client_socket.recv(1024).decode('utf-8')
        print(f'{client_number}: {msg}')
        for client in clients:
            client.send(f'{client_number}: {msg}'.encode('utf-8'))

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('0.0.0.0', 12345))
server.listen(5)

clients = []
client_number = 0
while True:
    client_socket, addr = server.accept()
    clients.append(client_socket)
    client_number += 1
    print(f'Accepted connection from {addr[0]}:{addr[1]}')
    client_handler = threading.Thread(target=handle_client, args=(client_socket, client_number))
    client_handler.start()
