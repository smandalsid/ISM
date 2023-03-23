from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
from stego_decode import *
from stego_encode import *

def encrypt(plaintext, filename):
    with open(filename, 'rb') as file:
        public_key = RSA.importKey(file.read())

    rsa_cipher = PKCS1_OAEP.new(public_key)
    ciphertext=rsa_cipher.encrypt(plaintext.encode())
    return ciphertext

def decrypt(filename, ciphertext):
    with open(filename, 'rb') as file:
        private_key=RSA.importKey(file.read(), 'password')

    rsa_cipher=PKCS1_OAEP.new(private_key)
    decrypted_text=rsa_cipher.decrypt(ciphertext)
    return decrypted_text.decode()


print("Enter your choice: ")
print("1. Encrypt and Encode")
print("2. Decode and Decrypt")
n=int(input())

if n==1:

    plaintext=input("\nEnter your message: ")
    ciphertext=encrypt(plaintext, 'audio/RSA/public_key.pem')
    print("\nEncrypted message: ")
    print(ciphertext)

        # src=input("\nEnter name of image file: ")
        # dest=input("Enter name of destination image file: ")
        # src='RSA/img.png'
        # dest='RSA/stego.png'
    Encode(ciphertext)
else:
    # dest=input("Enter name of image file: ")
    ciphertext2=Decode()
    print(ciphertext2)
    decrypted=decrypt('audio/RSA/private_key.pem', ciphertext2)
    print("\nDecrypted message: ")
    print(decrypted)

