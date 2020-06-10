from Crypto.Cipher import AES
from binascii import b2a_hex, a2b_hex

class AesCrypto():
    def __init__(self, key):
        self.key = key
        self.mode = AES.MODE_CBC

    def encrypt(self, text):
        text = text.encode('utf-8')
        cryptor = AES.new(self.key, self.mode, b'0000000000000000')
        length = 16
        count = len(text)
        if count < length:
            add = (length - count)
            text = text + ('\0' * add).encode('utf-8')
        elif count > length:
            add = (length - (count % length))
            text = text + ('\0' * add).encode('utf-8')
        self.ciphertext = cryptor.encrypt(text)
        return b2a_hex(self.ciphertext)

    def decrypt(self, text):
        cryptor = AES.new(self.key, self.mode, b'0000000000000000')
        a=a2b_hex(text)
        plain_text = cryptor.decrypt(a)
        return bytes.decode(plain_text).rstrip('\0')
