class HelloProtocol:

    @staticmethod
    def hello_connect(key: str) -> bytearray:  # HC + random 32 bytes encryption key
        data = bytearray(b"HC")
        data.extend(bytearray(key.encode()))

        return data

    @staticmethod
    def hello_server() -> bytearray:
        pass  # TODO: Implement
