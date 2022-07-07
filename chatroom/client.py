import socket
import time

PORT = 5050
SERVER = "localhost"
ADDR = (SERVER, PORT)
FORMAT = "utf-8"
DISCONNECT_MESSAGE = "!DISCONNECT"


def connect():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(ADDR)
    return client


def send(client, msg):
    message = msg.encode(FORMAT)
    client.send(message)


def start():
    clientusername = input('Enter a username to connect\n')
    connection = connect()
    while True:
        msg = input("Message (q for quit): ")

        if msg == 'q':
            break
        
        msg = f"{clientusername} : {msg}"
        send(connection, msg)

    send(connection, DISCONNECT_MESSAGE)
    time.sleep(1)
    print('Disconnected')


start()