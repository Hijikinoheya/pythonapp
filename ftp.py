from pyftpdlib.authorizers import DummyAuthorizer
from pyftpdlib.handlers import FTPHandler
from pyftpdlib.servers import FTPServer
import os

class FTPServerApp:
    def __init__(self, host, port, user, password, directory):
        self.host = host
        self.port = port
        self.user = user
        self.password = password
        self.directory = directory

    def run(self):
        authorizer = DummyAuthorizer()
        authorizer.add_user(self.user, self.password, self.directory, perm="elradfmw")
        handler = FTPHandler
        handler.authorizer = authorizer
        server = FTPServer((self.host, self.port), handler)
        print(f"FTP server started on {self.host}:{self.port}")
        server.serve_forever()

if __name__ == "__main__":
    host = input("Enter server host/IP: ")
    port = int(input("Enter server port: "))
    user = input("Enter username: ")
    password = input("Enter password: ")
    directory = input("Enter shared directory path: ")

    if not os.path.exists(directory):
        print("Directory does not exist. Please provide a valid directory path.")
    else:
        ftp_server = FTPServerApp(host, port, user, password, directory)
        ftp_server.run()
