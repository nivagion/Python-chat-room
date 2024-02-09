# -*- coding: utf-8 -*-
import socket
import threading

def receive_messages(sock):
    while True:
        msg = sock.recv(1024).decode('utf-8')
        username, _, text = msg.partition(':')
        if username.strip() != my_username:#ako je ime sa whitespaceom ispred onda usporeduje kao isto, npr " ivan" i "ivan" je isti string
            print(f'{msg}')

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

sendMsg = False #inace bi mogo slat odmah poruke 
isHost = input('are you host  y/n: ')
if isHost =='y':
    client.connect( ('localhost', 12345))#za hosta  
    sendMsg = True
else:
    gottenAddress = input('input forwarded adress (adress:port): ')
    addressPart, _, portPart = gottenAddress.partition(':')
    addressPart = addressPart.strip()
    portPart = portPart.strip()
    client.connect((addressPart, int(portPart)))
    sendMsg = True
#client.connect(('7.tcp.eu.ngrok.io', 14024))#u ovom formatu treba ngrok

if sendMsg == True:
    my_username = input('Enter username: ')
    client.send(my_username.encode('utf-8'))#šalje username

receive_handler = threading.Thread(target=receive_messages, args=(client,))#threada da moze primat poruke dok pises i saljes svoje
receive_handler.start()

while True and sendMsg == True:
    msg = input('')
    client.send(msg.encode('utf-8'))#šalje poruku
