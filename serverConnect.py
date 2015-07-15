from socket import *
class NetworkConnect:
    def __init__(self):
        self.host = "10.0.0.2" # set to IP address of target computer
        self.port = 13000
        self.addr = (self.host, self.port)
        self.buf = 1024
        self.flag = False
        self.serv = socket( AF_INET, SOCK_STREAM)
        self.serv.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
        self.serv.bind((self.addr))
        self.serv.listen(5)
        self.conn,self.addr = self.serv.accept()
        print("Connected...")
        self.flag = True

    def connection(self):        
        return self.flag

    def __enter__(self):
        return self

    def __exit__(self, type, value, traceback):
        print("Servers exit sommand")
        self.conn.close()
        self.serv.close()

    def receive(self):
        return str(self.conn.recv(self.buf))

    def send(self, message):
        self.conn.send(bytes(message,'utf-8'))
        
    def exit(self):
        self.conn.close()
        self.serv.close()
        
