class AccountProtocol:

    @staticmethod
    def bad_client_version(required_version: str) -> bytearray:
        packet = bytearray(b"AlEv")
        packet.extend(bytearray(required_version.encode()))

        return packet

    @staticmethod
    def access_denied() -> bytearray:
        return bytearray(b"AlEf")

    @staticmethod
    def account_banned() -> bytearray:
        return bytearray(b"AlEb")

    @staticmethod
    def already_connected() -> bytearray:
        return bytearray(b"AlEa")

    @staticmethod
    def community_information_message() -> bytearray:
        return bytearray(b"Ac0")

    @staticmethod
    def not_defined_nickname() -> bytearray:
        return bytearray(b"AlEr")

    @staticmethod
    def nickname_already_taken() -> bytearray:
        return bytearray(b"AlEs")

    @staticmethod
    def provide_nickname(nickname: str) -> bytearray:
        data_str = "Ad"+nickname

        return bytearray(data_str.encode())

    @staticmethod
    def queue_position(position: int, total_sub: int, total_no_sub: int, sub: bool, queue_id: int) -> bytearray:  # TODO: Implement
        packet = bytearray(b"Af")

        sub = 1 if sub else 0
        packet_data = str(position) + "|" + str(total_sub) + "|" + str(total_no_sub) + "|" + str(sub) + "|" + str(queue_id)

        packet.extend(bytearray(packet_data.encode()))

        return packet
