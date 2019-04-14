from pwn import *


def get_decrypted_msg(key):
    r = remote('chal1.swampctf.com', 1441)
    r.recvuntil('Pick your key, and pick wisely!\n')
    r.sendline(str(key))
    r.recv()
    r.sendline('2')
    r.recvuntil('What message would you like to decrypt (in hex)?\n')
    r.sendline('0' * 16 * 2 * 2)  # Two blocks of plaintext in hex
    r.recvuntil('<=')
    decrypted_msg = r.recvline().strip()
    r.close()
    return str(decrypted_msg, 'utf-8')


def get_flag(key):
    decrypted_msg = get_decrypted_msg(key)
    plaintext1 = decrypted_msg[:32]
    plaintext2 = decrypted_msg[32:]
    flag = int(plaintext1, 16) ^ int(plaintext2, 16)
    return bytes.fromhex(hex(flag)[2:])


print(get_flag(1) + get_flag(2) + get_flag(3))
