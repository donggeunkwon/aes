# AES; Advanced Encryption Standard

[![PyPI](https://img.shields.io/pypi/v/aes)](https://pypi.org/project/aes/) 
[![Downloads](https://pepy.tech/badge/aes)](https://pypi.org/project/aes/)
[![GitHub](https://img.shields.io/github/license/donggeunkwon/aes)](https://github.com/donggeunkwon/aes/blob/master/LICENSE)

A simple package for Advanced Encryption Standard(AES) Block Cipher [[pdf](http://csrc.nist.gov/publications/fips/fips197/fips-197.pdf)]

Version 1.2.0 is available. In this version, AES-128, 192, 256 with ECB, CBC, CTR mode are now supported!

## Install

You can easily install from PyPI.

```bash
$ pip install aes
```

After installation, open your python console and type
```python
from aes import aes

c = aes(0)
print(c.dec_once(c.enc_once(0)))
# print(c.decrypt(c.encrypt(0))) # for old version
```
If you get list of zeros, you are now ready to use __aes__ package!

```bash
Out[1]: [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
```

## Get Started
When a mode of operation is not necessary, just use enc_once/dec_once like:
```python
import aes

mk = 0x000102030405060708090a0b0c0d0e0f
pt = 0x00112233445566778899aabbccddeeff

cipher = aes.aes(mk, 128)
ct = cipher.enc_once(pt)
print(ct)
print("0x"+hex(aes.utils.arr8bit2int(ct))[2:].zfill(32))

pr = cipher.dec_once(ct)
print(pr)
print("0x"+hex(aes.utils.arr8bit2int(pr))[2:].zfill(32))
```

```bash
Out[1]: [105, 196, 224, 216, 106, 123, 4, 48, 216, 205, 183, 128, 112, 180, 197, 90]
Out[2]: 0x69c4e0d86a7b0430d8cdb78070b4c55a
Out[3]: [0, 17, 34, 51, 68, 85, 102, 119, 136, 153, 170, 187, 204, 221, 238, 255]
Out[4]: 0x00112233445566778899aabbccddeeff
```

Just want to use core functions:
```python
# example of using aes core function
mk_arr = aes.utils.int2arr8bit(mk, 16)
pt_arr = aes.utils.int2arr8bit(mk, 16)

rk_arr = aes.core.key_expansion(mk_arr, 128)

ct_arr = aes.core.encryption(pt_arr, rk_arr)
print("0x"+hex(aes.utils.arr8bit2int(ct_arr))[2:].zfill(32))

pr_arr = aes.core.decryption(ct_arr, rk_arr)
print("0x"+hex(aes.utils.arr8bit2int(pr_arr))[2:].zfill(32))
```

```bash
Out[1]: 0x0a940bb5416ef045f1c39458c653ea5a
Out[2]: 0x000102030405060708090a0b0c0d0e0f
```

With the mode of opearation:
```python
# example of using mode of operation
mk = 0x000102030405060708090a0b0c0d0e0f101112131415161718191a1b1c1d1e1f
mk_arr = aes.utils.int2arr8bit(mk, 32)
pt = 0x00112233445566778899aabbccddeeff
pt_arr = aes.utils.int2arr8bit(pt, 16)


cipher = aes.aes(mk, 256, mode='CTR', padding='PKCS#7')

# notice: enc/dec can only 'list'  !! 
ct_arr = cipher.enc(pt_arr)
print("0x"+hex(aes.utils.arr8bit2int(ct_arr))[2:].zfill(32))

pr_arr = cipher.dec(ct_arr)
print("0x"+hex(aes.utils.arr8bit2int(pr_arr))[2:].zfill(32))
```
```bash
Out[1]: 0xf235e46425db35cb300a528fbbe62697a55ca80972eb579044d786243219d7af
Out[2]: 0x00112233445566778899aabbccddeeff
```

It is great! But, if you didn't input the initial vector for 'CBC', 'CTR' mode, you get __Warning__:
```bash
/usr/local/lib/python3.7/dist-packages/aes/utils/_check_tools.py:59: UserWarning: Initail Vector is randomly selected: [23, 202, 118, 211, 113, 65, 4, 46, 115, 56, 211, 200, 177, 24, 127, 186] warnings.warn("Initail Vector is randomly selected: " + str(iv))
```
Don't forget to take the IV.
```python
print(cipher.iv) # save it!
```

------
### Version Summary
- v1.0.0 
- v1.0.1
  + Bug reported "__ModuleNotFoundError__", and fixed in this version.
- v1.2.0
  + Added AES-192, 256 and CBC, CTR mode.

------
### Report a bug to
Donggeun Kwon ([email](donggeun.kwon@gmail.com))
