from network.models.client import Client


class BaseHandler(object):

    def __init__(self, client: Client):
        self.client = client

        self.main_buffer = bytearray()
        self.packets_to_handle = list(bytearray())

    def __call__(self, *args, **kwargs):
        return BaseHandler(*args, **kwargs)

    def process_data(self, data: bytes) -> None:
        self.main_buffer.extend(data)

        previous_index = 0

        for current_index in range(len(self.main_buffer)):
            if data[current_index] == 0x0A and data[current_index+1] == 0x00:  # Delimiter
                self.packets_to_handle.append(data[previous_index:current_index])
                previous_index = current_index + 2  # Don't include delimiter

            if current_index == len(self.main_buffer) - 1:  # Last byte
                if data[current_index-1] == 0x0A and data[current_index] == 0x00:
                    del self.main_buffer[:]
                else:  # Bytes missing
                    del self.main_buffer[:previous_index]

            self.process_packets()

    def process_packets(self):
        for packet in self.packets_to_handle:
            packet_str = packet.decode()

            packet_type = packet_str[0]
            packet_sub_type = packet_str[1]

            self.handle(packet_type, packet_sub_type, packet_str[2:])

        del self.packets_to_handle[:]

    def receive_data(self, already_received_data: bytearray=None) -> str:
        data = bytearray(self.client.socket.recv(1024))

        if already_received_data is not None:
            data = already_received_data.extend(data)

        for index in range(len(data)):
            if data[index] == 0:
                return data[:index].decode()

        self.receive_data()

    def send_data(self, data: bytearray):
        data.append(0x0A)
        data.append(0x00)
        self.client.socket.send(data)

    def handle(self, packet_type: str, packet_subtype: str, data: str=None) -> None:
        raise NotImplementedError
