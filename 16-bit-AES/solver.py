from pwn import *
from Crypto.Cipher import AES


# Set up AES with the key we found
key = 'fLfLfLfLfLfLfLfL'
cipher = AES.new(key, AES.MODE_ECB)

# Connect to the server and give the answer!
c = remote("aes.sunshinectf.org", 4200)
c.recvuntil('Your text: \r\n')
c.sendline()
c.recvuntil('Ok, now encrypt this text with the same key: ')
plaintext = c.recvuntil('\r\n').strip()
ciphertext = cipher.encrypt(plaintext).hex()
print(f"Plaintext: {plaintext}\nCiphertext: {ciphertext}")
c.sendline(ciphertext)
print(c.recv())
c.close()
