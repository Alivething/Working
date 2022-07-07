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

def send(client):
    message = DISCONNECT_MESSAGE.encode(FORMAT)
    client.send(message)

def start():
    connection = connect()
    while True:
        msg = connection.recv(1024).decode(FORMAT)
        print(msg)