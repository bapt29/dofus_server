import socket
import threading
from typing import Tuple

from network.handlers.base_handler import BaseHandler
from network.handlers.authentication_handler import AuthenticationHandler

from network.models.client import Client


class Server:

    def __init__(self, port: int, handler: BaseHandler):
        self.port = port
        self.running = True
        self.handler = handler

        self.clients_list = list()

        self.main_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.main_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

        self.main_socket.bind(('0.0.0.0', port))
        self.listen()

    def listen(self) -> None:
        self.main_socket.listen(5)

        while True:
            client_socket, client_address = self.main_socket.accept()
            client_socket.settimeout(120)  # Connection is closed after 2 minutes without communication

            threading.Thread(target=self.handle_client, args=(client_socket, client_address)).start()

    def handle_client(self, client_socket: socket.socket, client_address: Tuple[str, int]) -> None:
        client = Client(client_socket, client_address)

        self.clients_list.append(client)
        handler = self.handler(client)

        while self.running:
            try:
                data = client_socket.recv(1024)

                if not data:
                    break

                handler.process_data(data)
            except socket.error as error:
                print(error)
                break

        client_socket.close()
        self.clients_list.remove(client)

    def stop(self):
        self.running = False


if __name__ == '__main__':
    server = Server(1234, AuthenticationHandler)
