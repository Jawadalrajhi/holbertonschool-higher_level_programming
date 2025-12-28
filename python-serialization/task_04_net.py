#!/usr/bin/env python3
"""Module for client-server communication with serialization.

This module implements a simple client-server application that
demonstrates serialization in network communication.
"""
import socket
import json


def start_server():
    """Start a server to receive serialized data.

    Sets up a server socket, listens for incoming connections,
    receives serialized data, deserializes it, and prints the result.
    """
    host = 'localhost'
    port = 65432

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(1)

    print("Server listening on {}:{}".format(host, port))

    conn, addr = server_socket.accept()
    print("Connected by {}".format(addr))

    data = conn.recv(1024)
    if data:
        received_dict = json.loads(data.decode('utf-8'))
        print("Received Dictionary from Client:")
        print(received_dict)

    conn.close()
    server_socket.close()


def send_data(data):
    """Send serialized data to the server.

    Args:
        data (dict): Python dictionary to send to the server.
    """
    host = 'localhost'
    port = 65432

    try:
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client_socket.connect((host, port))

        serialized_data = json.dumps(data)
        client_socket.sendall(serialized_data.encode('utf-8'))

        client_socket.close()
    except Exception as e:
        print("Error: {}".format(e))
