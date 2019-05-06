#-*- coding:utf-8 -*-
# 验证商品
# param base64PublicKey base64加密的公钥
# param signedData 数据
# param signature 签名
import base64

from Crypto.Hash import SHA
from Crypto.PublicKey import RSA
from Crypto.Signature import PKCS1_v1_5 as Signature_pkcs1_v1_5




def verifyPurchase(base64PublicKey, signedData, signature):
    if base64PublicKey == "" or signedData == "" or signature == "":
        return False;
    publicKey = generatePublicKey(base64PublicKey)
    return verify(publicKey, signedData, signature)


# 生成公钥
def generatePublicKey(base64PublicKey):
    try:
        return base64.b64decode(base64PublicKey)
    except Exception as e:
        return ""


# 验证签名
# param publicKey 公钥
# param signedData 需要验证的数据
# param signature 签名
def verify(publicKey, signedData, signature):
    try:
        decodeSig = base64.b64decode(signature)
    except Exception as e:

        return False

    try:
        rsakey = RSA.importKey(publicKey)

        verifier = Signature_pkcs1_v1_5.new(rsakey)

        digest = SHA.new()

        digest.update(signedData)

        is_verify = verifier.verify(digest, decodeSig)
    except Exception as e:
        is_verify = False

    return is_verify
