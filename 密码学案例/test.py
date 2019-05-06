#-*- coding:utf-8 -*-
from Crypto import Random
from Crypto.Hash import SHA
from Crypto.Cipher import PKCS1_v1_5 as Cipher_pkcs1_v1_5
from Crypto.Signature import PKCS1_v1_5 as Signature_pkcs1_v1_5
from Crypto.PublicKey import RSA
import base64


# 加密解密：公钥加密，私钥解密
#
# 签名验签：私钥签名，公钥验签
#
print ("1、生成私钥和公钥")

# 伪随机数生成器
random_generator = Random.new().read
# rsa算法生成实例
rsa = RSA.generate(2048, random_generator)
# A的秘钥对的生成
private_pem = rsa.exportKey()

with open('aaa-private.pem', 'wb') as f:
    f.write(private_pem)

public_pem = rsa.publickey().exportKey()
with open('aaa-public.pem', 'wb') as f:
    f.write(public_pem)

# B的秘钥对的生成
private_pem = rsa.exportKey()
with open('bbb-private.pem', 'wb') as f:
    f.write(private_pem)

public_pem = rsa.publickey().exportKey()
with open('bbb-public.pem', 'wb') as f:
    f.write(public_pem)

# 加密和解密
print ("2、加密和解密")
# A使用B的公钥对内容进行rsa 加密

message = '大家好，这就是我要加密的数据'
print ("message: " + message)
with open('bbb-public.pem') as f:
    key = f.read()
    rsakey = RSA.importKey(str(key))
    cipher = Cipher_pkcs1_v1_5.new(rsakey)
    cipher_text = base64.b64encode(cipher.encrypt(bytes(message.encode("utf8"))))
    print ("加密（encrypt）")
    print (cipher_text)

# B使用自己的私钥对内容进行rsa 解密

with open('bbb-private.pem') as f:
    key = f.read()
    rsakey = RSA.importKey(key)
    cipher = Cipher_pkcs1_v1_5.new(rsakey)
    text = cipher.decrypt(base64.b64decode(cipher_text), random_generator)
    print( "解密（decrypt）")
    print ("text:" + str(text,"utf8"))
    print("message:"+message)

    assert str(text,"utf8") == message

# 签名与验签
print ("3、 签名与验签")

# A使用自己的私钥对内容进行签名
print( "签名")
with open('aaa-private.pem') as f:
    key = f.read()
    rsakey = RSA.importKey(key)
    signer = Signature_pkcs1_v1_5.new(rsakey)
    digest = SHA.new()
    digest.update(message.encode("utf8"))
    sign = signer.sign(digest)
    signature = base64.b64encode(sign)

print(signature)
#B使用A的公钥进行验签
print ("验签")
with open('aaa-public.pem') as f:
    key = f.read()
    rsakey = RSA.importKey(key)
    verifier = Signature_pkcs1_v1_5.new(rsakey)
    digest = SHA.new()
    digest.update(message.encode("utf8"))
    is_verify = verifier.verify(digest, base64.b64decode(signature))
print (is_verify)