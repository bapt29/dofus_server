import string
import secrets


class Encryption:

    @staticmethod
    def generate_key() -> str:
        key = str()

        for i in range(32):
            key += secrets.choice(string.ascii_lowercase)

        return key


if __name__ == '__main__':
    print(Encryption.generate_key())
