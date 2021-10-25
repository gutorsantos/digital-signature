from Crypto.Cipher import AES

from generate_random import *


class __AES__:

    IV = ('6162636465666768696a6b6c6d6e6f70')
    key = 0
    def __init__(self):
        self.generate_key()

    def encrypt(self, text: str):
        padded = text + '0' * (16-len(text)%16)
        aes = AES.new(self.key[:16], AES.MODE_CBC, self.IV[:16])
        encrypted_msg = aes.encrypt(padded)
        # print(encrypted_msg.hex())
        return encrypted_msg

    def decrypt(self, text):
        aes = AES.new(self.key[:16], AES.MODE_CBC, self.IV[:16])
        m_padding = aes.decrypt(text)
        unpadded = m_padding
        return unpadded
    
    def generate_key(self):
        self.key = str(generate_random_int(128))