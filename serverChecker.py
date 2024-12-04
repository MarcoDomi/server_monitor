import socket
import ssl
import datetime
import pickle
import subprocess

class server:
    def __init__(self, name, port, type):
        self.name = name
        self.port = port
        self.type = type

        self.history = []