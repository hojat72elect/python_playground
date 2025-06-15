from cryptography.fernet import Fernet


def generate_key():
    return Fernet.generate_key()


def encrypt_message(key, message):
    cipher_suite = Fernet(key)
    encrypted_message = cipher_suite.encrypt(message.encode())
    return encrypted_message


def decrypt_message(key, encrypted_message):
    cipher_suite = Fernet(key)
    decrypted_message = cipher_suite.decrypt(encrypted_message).decode()
    return decrypted_message


class EncryptionHandler:
    def __init__(self, key=None):
        self.key = key if key is not None else self.generate_key()
        self.cipher_suite = Fernet(self.key)

    def generate_key(self):
        return Fernet.generate_key()

    def encrypt_message(self, message):
        if not isinstance(message, str):
            raise ValueError("Message must be a string")
        return self.cipher_suite.encrypt(message.encode())

    def decrypt_message(self, encrypted_message):
        if not isinstance(encrypted_message, bytes):
            raise ValueError("Encrypted message must be bytes")
        return self.cipher_suite.decrypt(encrypted_message).decode()


if __name__ == '__main__':
    encryption_handler = EncryptionHandler()

    input_message = input("Enter a message : ")
    encrypted = encryption_handler.encrypt_message(input_message)
    print(f"The encrypted message is this : {encrypted}")
    decrypted = encryption_handler.decrypt_message(encrypted)
    print(f"The decrypted message is this : {decrypted}")
