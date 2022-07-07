from flask import Flask, render_template
import threading
import socket
import listen

PORT = 5050
SERVER = "localhost"
ADDR = (SERVER, PORT)
FORMAT = "utf-8"
DISCONNECT_MESSAGE = "!DISCONNECT"

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)

clients = set()
clients_lock = threading.Lock()

listeneractive = False

def handle_client(conn, addr):
    print(f"[NEW CONNECTION] {addr} Connected")

    try:
        connected = True
        while connected:
            msg = conn.recv(1024).decode(FORMAT)
            if not msg:
                break

            if msg == DISCONNECT_MESSAGE:
                connected = False

            print(f"{msg}")
            with clients_lock:
                for c in clients:
                    c.send(f"{msg}".encode(FORMAT))

    finally:
        with clients_lock:
            clients.remove(conn)

        conn.close()


def start():
    print('[SERVER STARTED]!')
    server.listen()
    global listeneractive
    while True:
        conn, addr = server.accept()
        with clients_lock:
            clients.add(conn)
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()

        if len(clients) >= 1 and not listeneractive:
            listeneractive = True
            thread = threading.Thread(target=listen.start, args=())
            thread.start()

        if len(clients) == 1 and not listeneractive:
            listen.send()
            print("Empty Server")

start()