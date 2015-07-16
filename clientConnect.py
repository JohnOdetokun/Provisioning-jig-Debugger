import logging
from socket import *
class NetworkFailed(Exception):
    pass

class NetworkConnect:
    def __init__(self, logger=logging.getLogger(__name__)):
        self.logger = logger
        logging.basicConfig(level=logging.DEBUG)
        self.host = "10.0.0.1" # set to IP address of target computer
        self.port = 13000
        self.addr = (self.host, self.port)
        self.buf = 1024
        self.cli = socket( AF_INET, SOCK_STREAM)
        self.cli.connect((self.addr))
        logging.debug("Pi connected to laptop")
    def __enter__(self):
        return self
    def receive(self):
        return str(self.cli.recv(self.buf))
    def send(self, message):
        self.cli.send(bytes(message,'utf-8'))    
    def exit(self):
        self.conn.close()
        self.serv.close()
    def __exit__(self, type, value, traceback):
        logging.debug("clients exit command")
        self.cli.close()
