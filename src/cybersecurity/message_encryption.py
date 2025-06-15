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


if __name__ == '__main__':
    key = generate_key()
    input_message = input("Please enter a message to be encrypted: ")

    encrypted_message = encrypt_message(key, input_message)
    print(f"Encrypted message : {encrypted_message}")

    decrypted_message = decrypt_message(key, encrypted_message)
    print(f"Decrypted message : {decrypted_message}")
