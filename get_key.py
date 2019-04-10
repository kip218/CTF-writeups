from pwn import *
from Crypto.Cipher import AES


# We know that the padding is just 'x'
# We can get the ciphertext of 'xxxxxxxxxxxxxxxx', which is 'f4e8258d6c9930b9fc423b7df6c96739'
plaintext = 'x' * 16
ciphertext = 'f4e8258d6c9930b9fc423b7df6c96739'


def bruteforce_key(plaintext, ciphertext):
    for i in range(65, 123):
        for j in range(65, 123):
            key = chr(i) + chr(j)
            key *= 8
            cipher = AES.new(key, AES.MODE_ECB)
            msg = cipher.encrypt(plaintext)
            msg = msg.hex()
            if msg == ciphertext:
                print(f"Plaintext: {plaintext}\nCiphertext: {ciphertext}\nMsg: {msg}\nKey: {key}")


bruteforce_key(plaintext, ciphertext)

# The AES key is fLfLfLfLfLfLfLfL
# Time to write the solver!
