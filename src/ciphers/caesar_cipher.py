text = 'Hello Zaira'
shift = 3


def caesar(message, offset):
    """
    Encrypts a message using the Caesar Cipher. Caesar Cipher is a type of substitution cipher
    where each letter in the plaintext is 'shifted' a certain number of places down the alphabet.

    :param message: the original message .
    :param offset: the number of shifts in each letter.
    """

    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    encrypted_text = ''

    for char in message.lower():
        if char == ' ':
            encrypted_text += char
        else:
            index = alphabet.find(char)
            new_index = (index + offset) % len(alphabet)
            encrypted_text += alphabet[new_index]
    print('plain text:', message)
    print('encrypted text:', encrypted_text)


caesar(text, shift)
caesar(text, 13)
