class Client:

    def __init__(self, client_socket, client_address):
        self.socket = client_socket
        self.address = client_address

        self.user_id = None

        self.encryption_key = None

    def is_authenticated(self):
        return False if self.user_id else True
