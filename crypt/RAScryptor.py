from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import serialization, hashes
from cryptography.hazmat.primitives.asymmetric import padding, rsa


def load_public_key(public_key):
    """
    Loads a public key from the specified file in PEM format.
    :param public_key: The file path of the public key
    :return: A public key object
    """
    with open(public_key, "rb") as key_file:
        recipient_public_key = serialization.load_pem_public_key(
            key_file.read(),
            backend=default_backend()
        )
    return recipient_public_key


def encrypt_message(recipient_public_key, message):
    """
    Encrypts the message using the recipient's public key.
    :param recipient_public_key: The recipient's public key
    :param message: The message to be encrypted
    :return: The encrypted message
    """
    ciphertext = recipient_public_key.encrypt(
        message.encode(),
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )
    return ciphertext


def load_private_key(private_key):
    """
    Loads a private key from the specified file in PEM format.
    :param private_key: The file path of the private key
    :return: A private key object
    """
    with open(private_key, "rb") as key_file:
        recipient_private_key = serialization.load_pem_private_key(
            key_file.read(),
            password=None,
            backend=default_backend()
        )
    return recipient_private_key


def decrypt_message(recipient_private_key, ciphertext):
    """
    Decrypts the ciphertext using the recipient's private key.
    :param recipient_private_key: The recipient's private key
    :param ciphertext: The encrypted message
    :return: The decrypted message
    """
    plaintext = recipient_private_key.decrypt(
        ciphertext,
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )
    return plaintext

