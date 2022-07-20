# AES; Advanced Encryption Standard

[![PyPI](https://img.shields.io/pypi/v/aes)](https://pypi.org/project/aes/) 
[![PyPI - Downloads](https://img.shields.io/pypi/dm/aes)](https://pypi.org/project/aes/) 
[![GitHub](https://img.shields.io/github/license/donggeunkwon/aes)](https://github.com/donggeunkwon/aes/blob/master/LICENSE)

A simple package for Advanced Encryption Standard(AES) Block Cipher [[pdf](http://csrc.nist.gov/publications/fips/fips197/fips-197.pdf)]

Current version is only supported AES-128 with ECB mode. It will be updated.


## Install

You can easily install from PyPI.

```bash
$ pip install aes
```

After installation, open your python console and type
```python
import aes
```

## Get Started
```python
from aes import aes

mk = 0x000102030405060708090a0b0c0d0e0f
p  = 0x00112233445566778899aabbccddeeff

cipher = aes(mk)
cipher.encrypt(p)
```

```bash
Out[1]:  [105, 196, 224, 216, 106, 123, 4, 48, 216, 205, 183, 128, 112, 180, 197, 90]
```

If you want to return by int format.
```python
cipher.decrypt([105, 196, 224, 216, 106, 123, 4, 48, 216, 205, 183, 128, 112, 180, 197, 90], byte=True)
```

```bash
Out[2]: 88962710306127702866241727433142015
```


------
### Version
- v1.0.0 
- v1.0.1
  + Bug reported "__ModuleNotFoundError__", and fixed in this version.


------
### Bug Report
Donggeun Kwon ([email](donggeun.kwon@gmail.com))
