from pwn import *


# get ciphertext from the challenge server with our plaintext
def get_cipher(plaintext):
    address = "aes.sunshinectf.org"
    port = 4200
    c = remote(address, port)
    c.recvuntil('Your text: \r\n')
    c.sendline(plaintext)
    cipher = c.recv().strip()
    c.close()
    return cipher


# bruteforce a character of the padding
def brute_char(num, known_padding):
    c_padded = get_cipher('A' * num + known_padding)
    for i in range(256):
        payload = 'A' * num + known_padding
        payload += chr(i)
        c_test = get_cipher(payload)
        if c_padded == c_test:
            return chr(i)


# bruteforce the padding
def brute_padding():
    known_padding = ''
    for i in range(15, -1, -1):
        char = brute_char(i, known_padding)
        known_padding += char
    return known_padding


padding = brute_padding()
print(padding)

# The padding is 'x'
