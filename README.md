# AES; Advanced Encryption Standard

Implementation of Advanced Encryption Standard (AES) Block Cipher



```python
from aes import aes

mk = 0x000102030405060708090a0b0c0d0e0f

cipher = aes(mk)
cipher.encrypt(0x00112233445566778899aabbccddeeff)
```

[105, 196, 224, 216, 106, 123, 4, 48, 216, 205, 183, 128, 112, 180, 197, 90]



```python
cipher.decrypt([105, 196, 224, 216, 106, 123, 4, 48, 216, 205, 183, 128, 112, 180, 197, 90], byte=True)
```

88962710306127702866241727433142015