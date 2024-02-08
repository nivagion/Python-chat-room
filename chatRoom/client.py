import socket
import threading

def receive_messages(sock):
    while True:
        msg = sock.recv(1024).decode('utf-8')
        username, _, text = msg.partition(':')
        if username.strip() != my_username:#ako je ime sa whitespaceom ispred onda usporeduje kao isto, npr " ivan" i "ivan" je isti string
            print(f'{msg}')

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#client.connect(('7.tcp.eu.ngrok.io', 14024))#u ovom formatu treba ngrok
client.connect(('localhost', 12345))#za hosta

my_username = input('Enter username: ')
client.send(my_username.encode('utf-8'))#šalje username

receive_handler = threading.Thread(target=receive_messages, args=(client,))#threada da moze primat poruke dok pises i saljes svoje
receive_handler.start()

while True:
    msg = input('')
    client.send(msg.encode('utf-8'))#šalje poruku
