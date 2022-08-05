# -*- coding: utf-8 -*-
"""
Created on Thu Aug  4 13:52:04 2022


@author: Donggeun Kwon (donggeun.kwon at gmail.com)

Cryptographic Algorithm Lab.
Institute of Cyber Security & Privacy(ICSP), Korea Univ.
"""

from ..core.para import STATE_LEN

from ..core._core import encryption
from ..core._core import decryption
from ..core._core import key_expansion

from ..utils._format_tools import arr8bit2int
from ..utils._format_tools import int2arr8bit


# electronic codebook
class ECB(object):
    def __init__(self, mk, iv=None):
        self.rk = key_expansion(mk)
        
    def enc(self, pt):
        return encryption(pt, self.rk)
    
    def dec(self, ct):
        return decryption(ct, self.rk)
    
# cipher block chaining    
class CBC(object):
    def __init__(self, mk, iv):
        self.rk = key_expansion(mk)
        self.iv = iv

    def _xor_arr(self, a, b):
        c = []
        for i in range(len(a)):
            c.append(a[i] ^ b[i])
        return c
        
    def enc(self, pt):
        st = self._xor_arr(pt, self.iv)
        ct = encryption(st, self.rk)
        self.iv = ct
        return ct
    
    def dec(self, ct):
        st = decryption(ct, self.rk)
        pt = self._xor_arr(st, self.iv)
        self.iv = ct
        
        return pt
    
# counter mode
class CTR(object):
    def __init__(self, mk, iv, cnt=1):
        self.rk = key_expansion(mk)
        self.iv = iv
        self.c = cnt
        
    def _xor_arr(self, a, b):
        c = []
        for i in range(len(a)):
            c.append(a[i] ^ b[i])
        return c
    
    def enc(self, pt):
        st = encryption(self.iv, self.rk)
        ct = self._xor_arr(st, pt)
        self.iv = int2arr8bit(arr8bit2int(self.iv)+self.c, STATE_LEN)
        
        return ct
    
    def dec(self, ct):
        st = encryption(self.iv, self.rk)
        pt = self._xor_arr(st, ct)
        self.iv = int2arr8bit(arr8bit2int(self.iv)+self.c, STATE_LEN)
        
        return pt