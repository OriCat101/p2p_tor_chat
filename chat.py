import socket
import threading


def listen(ip, port):
    """
    Listens on the specified port for an incoming connection.
    IP is optional
    """
    if ip == "":
        ip = "0.0.0.0"

    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((ip, port))
    server.listen()

    # client, _ = server.accept()
    return server.accept()


def connect(ip, port):
    """
    Connects to another client using the given port and IP.
    """
    # client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((ip, port))


def sending_messages(c):
    while True:
        message = input("")
        c.send(message.encode())
        print("You: " + message)


def receiving_messages(c):
    while True:
        data = c.recv(1024).decode()
        if data != "":
            print("Partner: " + data)


choice = input("Do you want to host (1) or to connect (2): ")
if choice == "1":
    client, _ = listen("0.0.0.0", 9999)

elif choice == "2":
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    connect("localhost", 9999)

threading.Thread(target=sending_messages, args=(client,)).start()
threading.Thread(target=receiving_messages, args=(client,)).start()
