import socket
import threading

from colorama import Fore, Style


def listen(ip, port):
    """
    Listens on the specified IP and port for an incoming connection.
    :param ip: The IP address to listen on. Default is '0.0.0.0'
    :param port: The port to listen on
    :return: A tuple containing the client socket and the address of the client
    """
    if ip == "":
        ip = "0.0.0.0"

    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((ip, port))
    server.listen()

    return server.accept()


def connect(ip, port):
    """
    Connects to another client using the given IP and port.
    :param ip: The IP address of the other client
    :param port: The port of the other client
    :return: None
    """
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((ip, port))
    return client


def sending_messages(c, input_prompt):
     """
    Sends messages to the connected client
    :param c: The client socket
    :param input_prompt: The prompt to be displayed before sending a message
    :return: None
    """
    while True:
        message = input(input_prompt)
        c.send(message.encode())
        print("You: " + message)


def receiving_messages(c, input_prompt):
    """
    Receives messages from the connected client
    :param c: The client socket
    :param input_prompt: The prompt to be displayed after receiving a message
    :return: None
    """
    while True:
        data = c.recv(1024).decode()
        if data != "":
            print("Partner: " + data)
            print(input_prompt)


def display_ip():
    """
    Display the IP address of the system in red
    :return: None
    """
    hostname = socket.gethostname()
    ip_address = socket.gethostbyname(hostname)
    print("Your IP address is: " + Fore.RED + ip_address + Style.RESET_ALL)

input_prompt = ">>"

choice = input("Do you want to host (1) or to connect (2): ")
if choice == "1":
    display_ip()
    client, _ = listen("0.0.0.0", 9999)

elif choice == "2":
    client = connect("localhost", 9999)

threading.Thread(target=sending_messages, args=(client,)).start()
threading.Thread(target=receiving_messages, args=(client,)).start()
