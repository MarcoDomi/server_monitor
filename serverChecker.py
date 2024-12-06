import socket
import ssl
import datetime
import pickle
import subprocess

class server:
    def __init__(self, name, port, type):
        self.name = name
        self.port = port
        self.connectionType = type

        self.history = []
    
    def add_history(self, item):
        max_history = 100

        if len(self.history) == max_history:
            self.history.pop()

        self.history.insert(0, item)

def checkConnection(server):
    try:
        if server.connectionType == "plain":
            socket.create_connection((server.name, server.port), timeout=10)
            print(f"Connected to {server.name} on port {server.port} on a plain connection")
        elif server.connectionType == "ssl":
            context = ssl.create_default_context()
            context.wrap_socket(socket.create_connection((server.name, server.port), timeout=10), server_hostname=server.name)
            print(f"Connected to {server.name} on port {server.port} on a secure connection")
        elif server.connectionType == "ping":
            subprocess.check_output(f"ping -c 1 {server.name}", shell=True, universal_newlines=True)
            print(f"Pinged {server.name}")
    except TimeoutError:
        print("Connection timed out")
    except:
        print("Unknown error?")


s = server("redsddit.com", 443, 'ssl')

checkConnection(s)
