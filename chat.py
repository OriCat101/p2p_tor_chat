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
    #if ip == "":
    #    ip = "0.0.0.0"
    #if port == "":
    #    port = "9999"

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
    return ip_address


def is_valid_ip_port(ip_port):
    """
    Check if the given IP address and port are valid
    :param ip_port: The IP address and port to check in the format "ip:port"
    :return: True if the IP address and port are valid, False otherwise
    """
    try:
        ip, port = ip_port.split(':')
        socket.inet_pton(socket.AF_INET, ip)
        if 0 <= int(port) <= 65535:
            return True
        else:
            return False
    except (socket.error, ValueError):
        return False


input_prompt = ">>"

choice = input("Do you want to host (1) or to connect (2): ")
if choice == "1":
    print("Your IP address is: " + Fore.RED + display_ip() + Style.RESET_ALL)
    ip_port = input("Enter the IP and port to listen on (default is: 0.0.0.0:9999): ")
    if ip_port == "":
        ip_port = "0.0.0.0:9999"
    if is_valid_ip_port(ip_port):
        ip, port = ip_port.split(":")
        client, _ = listen(ip, int(port))
    else:
        print("Invalid IP address or port")

elif choice == "2":
    ip_port = input("Enter the IP and port to connect to (e.g. 0.0.0.0:9999): ")
    if is_valid_ip_port(ip_port):
        ip, port = ip_port.split(":")
        client = connect(ip, int(port))
    else:
        print("Invalid IP address or port")

threading.Thread(target=sending_messages, args=(client,)).start()
threading.Thread(target=receiving_messages, args=(client,)).start()
