from base64 import b32encode, b32decode
import hashlib
from Crypto.Cipher import DES
from stego import *

password = "Password"
salt = '\x28\xAB\xBC\xCD\xDE\xEF\x00\x33'
key = password + salt
m = hashlib.md5(key.encode("utf-8"))
key = m.digest()
(dk, iv) =(key[:8], key[8:])

print("Audio steganography")
print("Enter you choice:")
print("1. Encrypt and Encode")
print("2. Decode and Decrypt")
n=int(input())

if n==1:
    crypter = DES.new(dk, DES.MODE_CBC, iv)

    plain_text= input("Enter message: ")

    print("The plain text is : ",plain_text)
    plain_text += '\x00' * (8 - len(plain_text) % 8)
    ciphertext = crypter.encrypt(plain_text.encode("utf-8"))
    encode_string= b32encode(ciphertext)
    print("The encrypted string is : ", encode_string.decode("utf-8"))
    
    src=input("Enter name of image file to encode in: ")
    dest=input("Enter name of new image file: ")
    Encode(src, encode_string.decode("utf-8"), dest)
    print("Encrpyted message encoded")
    
else:
    file=input("Enter name of image file: ")
    encode_string=Decode(file)
    crypter = DES.new(dk, DES.MODE_CBC, iv)
    encrypted_string=b32decode(encode_string)
    decrypted_string = crypter.decrypt(encrypted_string)
    print("The decrypted string is : ",decrypted_string.decode("utf-8"))


