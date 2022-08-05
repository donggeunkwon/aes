# -*- coding: utf-8 -*-
"""

v1.0.0 
- (2019.07.17)
v1.0.1
- Bug reported "ModuleNotFoundError", thus __init__.py file is created.
v1.2.0 
- The table 'sbox, rsbox, rcon' replaced to functions.
- 'encrypt' and 'decrypt' functions will be replaced with 'enc' and 'dec' respectively.
- AES-192, 256 with CBC CTR mode


@author: Donggeun Kwon (donggeun.kwon at gmail.com)
"""

__locals__ = ['__locals__'] + list(locals()) # dir()

# class
from ._aes import aes
from . import core
from . import utils

# var
__doc__ = 'http://csrc.nist.gov/publications/fips/fips197/fips-197.pdf'
__version__ = "1.2.0"
__all__ = [n for n in list(dir()) if n not in __locals__]

# remove __locals__
del __locals__