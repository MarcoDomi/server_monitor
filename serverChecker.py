import socket
import ssl
from datetime import datetime
import pickle
import subprocess
import os

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
    success = False
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
        success = True
    except TimeoutError:
        print("Connection timed out")
    except:
        print("Unknown error?")

    return success

def main():

    if os.path.exists('server_data.pickle'):
        file = open("server_data.pickle", "rb")
        servers = pickle.load(file)
        file.close()
    else: 
        servers = [
            server("reddit.com", 443, "ssl"),
            server("google.com", 80, "plain"),
            server("youtube.com", 80, "ping"),
            server("wikipedia.org", 443, "ssl"),
        ]
    
    for s in servers:
        connection_result = checkConnection(s)
        s.add_history(f"{s.name} - Date: {datetime.now()} - Connection result: {connection_result}")
        print(len(s.history))


main()