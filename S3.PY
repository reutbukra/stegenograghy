from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
import binascii

keyPair = RSA.generate(3072)
pubKey = keyPair.publickey()
f = open("MyRSA.txt",'w')
f.write(pubKey.exportKey('PEM'))
f.close()

f = open("MyRSA.txt",'r')
key = RSA.importKey(f.read())

pubKeyPEM = pubKey.exportKey()
privKePEM = keyPair.exportKey()

#-----------------------------

msg = b'A message for encryption'
encryptor = PKCS1_OAEP.new(RSA.importKey(pubKeyPEM))
encrypted = encryptor.encrypt(msg)

#-----------------------------
decryptor = PKCS1_OAEP.new(keyPair)
decrypted = decryptor.decrypt(encrypted)
print('Decrypted:', decrypted)