from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP


keypair = RSA.generate(3072)
pubkey = keypair.publickey()

with open("image/RSA/public_key.pem", 'wb') as file:
    file.write(pubkey.exportKey('PEM'))
    file.close()

with open("image/RSA/private_key.pem", 'wb') as file:
    file.write(keypair.exportKey('PEM', 'password'))
    file.close()