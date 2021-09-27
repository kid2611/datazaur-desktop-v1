
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.fernet import Fernet
import base64


class Cryptozaur:
    # encrypts symmetrically
    @staticmethod
    def symmetric_encrypt(data, key):
        return Fernet(key).encrypt(data.encode())

    @staticmethod
    # decrypts symmetrically
    def symmetric_decrypt(data, key):
        return Fernet(key).decrypt(data).decode()

    # derives encryption key for symmetric encryption from password using PBKDF2HMAC
    @staticmethod
    def derive_key(password, salt):
        return base64.urlsafe_b64encode(PBKDF2HMAC(algorithm=hashes.SHA256(), length=32, salt=salt, iterations=100000,
                                                   backend=default_backend()).derive(password.encode()))