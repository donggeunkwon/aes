# -*- coding: utf-8 -*-
"""
Updated on Wed Jul 20 13:10:42 2022

    AES; block cipher

@author: Donggeun Kwon (donggeun.kwon at gmail.com)
"""

import os

from .utils._format_tools import int2arr8bit
from .utils._format_tools import arr8bit2int
from .utils._format_tools import bytes2int
from .utils._format_tools import int2bytes

from .core.para import STATE_LEN

KEY_SIZE_128_LEN = 16
KEY_SIZE_192_LEN = 24
KEY_SIZE_256_LEN = 32

class aes(object): # Advanced Encryption Standard
    def __init__(self, 
                 masterkey, 
                 keysize=128, 
                 mode='ECB',
                 padding='PKCS#7',
                 iv=None):
        from .utils._check_tools import check_para
        _, mk, mod, pad, iv = check_para(keysize,
                                         masterkey,
                                         mode,
                                         padding,
                                         iv)
        self.iv = iv
        self.mk = mk
        self.mode = mod
        self.padding = pad

    # enc/dec without mode of operation
    def enc_once(self, pt:list) -> list:
        from .core._core import encryption, key_expansion

        pt = int2arr8bit(pt, STATE_LEN)
        rk = key_expansion(self.mk)

        return encryption(pt, rk)

    def dec_once(self, ct:list) -> list:
        from .core._core import decryption, key_expansion

        ct = int2arr8bit(ct, STATE_LEN)
        rk = key_expansion(self.mk)

        return decryption(ct, rk)

    #######################################################################
    # mode of operation
    def enc(self, plaintexts:list, verbose=False):
        # size
        s = len(plaintexts)
        p = (s % STATE_LEN)

        if verbose:
            try: from tqdm import tqdm
            except:
                import warnings
                warnings.warn("can't find module 'tqdm'")
                forloop = range(s//STATE_LEN)
            else:
                forloop = tqdm(range(s//STATE_LEN))
        else: forloop = range(s//STATE_LEN)

        # mode of operation setting
        Mode = self.mode(self.mk, self.iv)
        ciphertexts, i = [], -1

        # encryption
        for i in forloop:
            pt = plaintexts[STATE_LEN*i:STATE_LEN*(i+1)]
            ct = Mode.enc(pt)
            ciphertexts = ciphertexts + ct

        # padding
        # format
        if i==-1:
            pt = plaintexts
        else:
            pt = plaintexts[STATE_LEN*(i+1):]
        
        pt = int2arr8bit(arr8bit2int(pt), p)
        # padding
        pt = self.padding(pt, STATE_LEN)
        # encryption
        ct = Mode.enc(pt)
        ciphertexts = ciphertexts + ct

        return ciphertexts

    def dec(self, ciphertexts, verbose=False):
        # size
        s = len(ciphertexts)
        assert (s % STATE_LEN)==0

        if verbose:
            try: from tqdm import tqdm
            except:
                import warnings
                warnings.warn("can't find module 'tqdm'")
                forloop = range((s//STATE_LEN)-1)
            else:
                forloop = tqdm(range((s//STATE_LEN)-1))
        else: forloop = range((s//STATE_LEN)-1)

        # mode of operation setting
        Mode = self.mode(self.mk, self.iv)
        plaintexts = []

        # encryption
        for i in forloop:
            ct = ciphertexts[STATE_LEN*i:STATE_LEN*(i+1)]
            pt = Mode.dec(ct)
            plaintexts = plaintexts + pt

        # unpadding
        ct = ciphertexts[-16:]
        pt = Mode.dec(ct)
        pt = self.padding(pt, STATE_LEN, unpad=True)
        plaintexts = plaintexts + pt

        return plaintexts
    
    '''
    # support file system
    def enc_file(self, 
                 src_path:str, 
                 dst_path:str, 
                 verbose=True):
        if not os.path.isfile(src_path):
            raise FileExistsError("can't find "+str(src_path))
        
        s = os.path.getsize(src_path)
        p = (s % STATE_LEN)
        plain  = open(src_path, mode='rb')
        cipher = open(dst_path, mode='wb')

        if verbose:
            try: from tqdm import tqdm
            except:
                import warnings
                warnings.warn("can't find module 'tqdm'")
                forloop = range(s//STATE_LEN)
            else:
                name = os.path.split(src_path)[1]
                forloop = tqdm(range(s//STATE_LEN), desc=name)
        else: forloop = range(s//STATE_LEN)

        Mode = self.mode(self.mk, self.iv)

        for _ in forloop:
            # read
            pt = plain.read(STATE_LEN)
            # format
            pt = bytes2int(pt)
            pt = int2arr8bit(pt, STATE_LEN)
            # encryption
            ct = Mode.enc(pt)
            # format
            ct = arr8bit2int(ct)
            ct = int2bytes(ct, STATE_LEN)
            # save
            cipher.write(ct)

        # read all
        pt = plain.read()
        # format
        pt = bytes2int(pt)
        pt = int2arr8bit(pt, p)
        # padding
        pt = self.padding(pt, STATE_LEN)
        # encryption
        ct = Mode.enc(pt)
        # format
        ct = arr8bit2int(ct)
        ct = int2bytes(ct, STATE_LEN)
        # write
        cipher.write(ct)

        # close files
        plain.close()
        cipher.close()

        return True

    def dec_file(self, 
                 src_path:str, 
                 dst_path:str, 
                 verbose=True):
        if not os.path.isfile(src_path):
            raise FileExistsError("can't find "+str(src_path))
        
        s = os.path.getsize(src_path)
        assert (s % STATE_LEN)==0

        plain  = open(dst_path, mode='wb')
        cipher = open(src_path, mode='rb')

        if verbose:
            try: from tqdm import tqdm
            except:
                import warnings
                warnings.warn("can't find module 'tqdm'")
                forloop = range(s//STATE_LEN)
            else:
                name = os.path.split(src_path)[1]
                forloop = tqdm(range(s//STATE_LEN), desc=name)
        else: forloop = range(s//STATE_LEN)

        Mode = self.mode(self.mk, self.iv)

        for _ in forloop:
            # read
            ct = cipher.read(STATE_LEN)
            # format
            ct = bytes2int(ct)
            ct = int2arr8bit(ct, STATE_LEN)
            # encryption
            pt = Mode.dec(ct)
            # format
            pt = arr8bit2int(pt)
            pt = int2bytes(pt, STATE_LEN)
            # save
            plain.write(pt)

        # close files
        plain.close()
        cipher.close()

        return True
    '''

    #########################################################################
    def encrypt(self, pt, byte=False):
        import warnings
        warnings.simplefilter('once', FutureWarning)
        warnings.warn("The function 'encrypt' will remove, use 'enc_once'.", FutureWarning)
        
        from .core._core import encryption, key_expansion

        pt = int2arr8bit(pt, STATE_LEN)
        rk = key_expansion(self.mk)
        ct = encryption(pt, rk)

        if not byte: return ct
        return arr8bit2int(ct)
    
    def decrypt(self, ct, byte=False):
        import warnings
        warnings.simplefilter('once', FutureWarning)
        warnings.warn("The function 'decrypt' will remove, use 'dec_once'.", FutureWarning)

        from .core._core import decryption, key_expansion

        ct = int2arr8bit(ct, STATE_LEN) # force to size 16
        rk = key_expansion(self.mk)
        pt = decryption(ct, rk)

        if not byte: return pt
        return arr8bit2int(pt)
        