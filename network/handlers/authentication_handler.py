from network.handlers.base_handler import BaseHandler

from utils.encryption import Encryption

from network.protocol.hello_protocol import HelloProtocol
from network.protocol.account_protocol import AccountProtocol


class AuthenticationHandler(BaseHandler):

    def __init__(self, client):  # Exception first packets are not formatted like others
        super().__init__(client)

        self.client.encryption_key = Encryption.generate_key()
        self.send_data(HelloProtocol.hello_connect(self.client.encryption_key))

        self.version = self.receive_data()
        self.credentials = self.receive_data()

    def handle(self, packet_type: str, packet_subtype: str, data: str = None) -> None:
        if packet_type == 'A':
            if packet_subtype == 'f':
                if not self.client.is_authenticated():
                    self.authenticate()
                else:
                    self.send_data(AccountProtocol.queue_position(1, 1, 0, True, 1))
            elif packet_subtype == '':
                pass

    def authenticate(self):
        self.client.user_id = 1
        username, password = self.credentials.split("#")
        username = username[:-1]

        print("Username:", username)
        print("Password:", password)

    def define_nickname(self):
        self.send_data(AccountProtocol.not_defined_nickname())
        nickname = self.receive_data()

        print("Nickname", nickname)
