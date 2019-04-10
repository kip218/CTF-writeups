# [SunshineCTF 2019 : 16-bit-AES](https://2019.sunshinectf.org/challenges#16-bit-AES)

**Category:** Crypto  
**Points:** 100  
**Author:** ps_iclimbthings  
**Description:**  
> Why so small?
>
> nc archive.sunshinectf.org 19003

## Write-up

There were two ways of solving this challenge. One way was much easier than the other, and I doubt it was the intended solution.  
I will first explain the proper way, and then go over the easier way.

### Challenge explanation

When I first connect to the server, I get the following message: 

![](image1.png)

After sending some text, it asks me to encrypt some randomly generated text with the same key: 

![](image2.png)

If I give it the correctly encrypted ciphertext, it will give me the flag.

### Challenge solution

