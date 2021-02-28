# -*- coding: utf-8 -*-
# @Author: zhazhafang
# @Blog: http://blog.zhazhafang.cn

from Crypto.Cipher import AES
from binascii import b2a_hex, a2b_hex
import json


class prpcrypt():
    def __init__(self, key, iv):
        self.key = key
        self.iv = iv
        self.mode = AES.MODE_CBC

    def decrypt(self, text):
        cryptor = AES.new(self.key, self.mode, self.iv)
        plain_text = cryptor.decrypt(a2b_hex(text))
        plain_text = plain_text.decode('UTF-8', 'ignore').strip().strip(b'\x00'.decode())
        plain_text = json.loads(plain_text)
        return plain_text



if __name__ == '__main__':
    iv = "8749576b52974246" # iv
    pc = prpcrypt('9987d634a86256198e52a471c47ca446', iv)  # 初始化密钥 和 iv
    d = pc.decrypt("35271f595b38d9b6481c91c6c11625a192541d8feb0bf53b6703209c7f3c210ff7a63f01f09c9ee45964c5f64dc1df5212e49541bef9ce30754675697a5aeee52c42fc2ffcd68eb20f45ebbd8caf976c")  # 解密
    print(d)