#-*- coding:utf-8 -*-
from Crypto.Cipher import AES


def aes_cbc_encrypt(plaintext, key, iv):
    """AES加密CBC模式演示"""
    aes_cryptor = AES.new(key, AES.MODE_CBC, iv)
    return aes_cryptor.encrypt(plaintext)


def aes_cbc_decrypt(ciphertext, key, iv):
    """AES解密CBC模式演示"""
    aes_cryptor = AES.new(key, AES.MODE_CBC, iv)
    return aes_cryptor.decrypt(ciphertext)


aes128_key = b'\x7d\xef\x87\xd5\xf8\xbb\xff\xfc\x80\x91\x06\x91\xfd\xfc\xed\x69'
aes128_iv = b'\x73\x7e\xa2\xcb\x61\x6d\x40\x6f\xd5\xb4\x32\xa2\xc8\xc5\x8e\xfa'
plain_text = 'aesAlgorithmDemo'
cipher_text = aes_cbc_encrypt(plain_text, aes128_key, aes128_iv)
origin = aes_cbc_decrypt(cipher_text, aes128_key, aes128_iv)
print(origin)