from cryptography.hazmat.primitives import serialization, hashes
from cryptography.hazmat.primitives.asymmetric import padding, rsa


def load_public_key(public_key):
    # Load the recipient's public key
    with open(public_key, "rb") as key_file:
        recipient_public_key = serialization.load_pem_public_key(
            key_file.read(),
            backend=default_backend()
        )
    return recipient_public_key


def encrypt_message(recipient_public_key):
    # Encrypt the message
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
    # Load the recipient's private key
    with open(private_key, "rb") as key_file:
        recipient_private_key = serialization.load_pem_private_key(
            key_file.read(),
            password=None,
            backend=default_backend()
        )
    return recipient_private_key


def decrypt_message(recipient_private_key)
    # Decrypt the message
    plaintext = recipient_private_key.decrypt(
        ciphertext,
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )
    return plaintext
