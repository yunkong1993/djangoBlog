from Crypto.Cipher import AES
from binascii import b2a_hex, a2b_hex


def encrypt_string(message):
    encode_result = ""
    for char in message:
        char_int = ord(char)
        if char.isalpha():  # 判断是否为字母
            if 64 < char_int < 78 or 96 < char_int < 110:  # 针对其中的部分字母进行加密
                encode_result += "00" + str((char_int + 13) * 2) + "|"
            else:  # 对剩下字母进行加密
                encode_result += "01" + str(char_int - 23) + "|"

        elif '\u4e00' <= char <= '\u9fff':  # 单个汉字可以这么判断
            encode_result += "02" + str(char_int + 24) + "|"
        else:  # 对数字、特殊字符进行加密
            encode_result += "03" + str(char_int) + "|"
    return encode_result


def decrypt_string(message):
    decode_result = ""

    # 将message转换为list
    message_list = message.split("|")
    message_list.remove("")  # 移除list中的空元素

    for i in message_list:
        type_ = i[:2]
        char_number = int(i[2:])
        if type_ == "00":
            char_number = int(char_number / 2 - 13)
        elif type_ == "01":
            char_number = char_number + 23
        elif type_ == "02":
            char_number = char_number - 24
        else:
            char_number = char_number

        decode_result += chr(char_number)
    return decode_result


class AesCrypto():
    def __init__(self, key, IV):
        self.key = key
        self.iv = IV
        self.mode = AES.MODE_CBC

    # 加密函数，text参数的bytes类型必须位16的倍数，不够的话，在末尾添加"\0"(函数内以帮你实现)
    def encrypt(self, text):
        cryptor = AES.new(self.key, self.mode, self.iv)  # self.key的bytes长度是16的倍数即可， self.iv必须是16位
        length = 16
        count = len(text)
        if (count % length != 0):
            add = length - (count % length)
        else:
            add = 0

        text = text + ("\0".encode() * add)  # 这里的"\0"必须编码成bytes，不然无法和text拼接

        self.ciphertext = cryptor.encrypt(text)
        return (self.ciphertext)

    def decrypt(self, text):
        cryptor = AES.new(self.key, self.mode, self.iv)
        plain_text = cryptor.decrypt((text)).decode()
        return plain_text
