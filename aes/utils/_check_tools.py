# -*- coding: utf-8 -*-

from ..core.para import STATE_LEN, KEY_SIZE_LIST
from ..core.para import MODE_OF_OPERATION_LIST
from ..core.para import PADDING_LIST

from ..utils._format_tools import int2arr8bit
from ..utils._format_tools import arr8bit2int
from ..utils._format_tools import bytes2int


def check_para(keysize, masterkey, mode, padding, iv):
    # check key size
    keysize = keysize
    if keysize not in KEY_SIZE_LIST:
        from ..utils._error_tools import KeysizeError
        raise KeysizeError(keysize)
    
    # make key value's size equals key size
    mk = int2arr8bit(masterkey, keysize//8)
    
    # mode of operation setting
    if mode not in MODE_OF_OPERATION_LIST:
        from ..utils._error_tools import ModeofOperationError
        raise ModeofOperationError(mode)    
    if mode=='ECB':
        from ..mode._mode import ECB
        mod = ECB
    elif mode=='CBC':
        from ..mode._mode import CBC
        mod = CBC
    elif mode=='CTR':
        from ..mode._mode import CTR
        mod = CTR
    else: raise NotImplementedError

    # padding setting
    if padding not in PADDING_LIST:
        from ..utils._error_tools import PaddingError
        raise PaddingError(padding)
    if padding == 'PKCS#7':
        from ..mode._padding import pkcs_padding
        padding = pkcs_padding
    elif padding == 'byte':
        from ..mode._padding import byte_padding
        padding = byte_padding
    else: raise NotImplementedError
    
    # initial vector setting
    if iv is None:
        try:
            import random
            iv = int2arr8bit(bytes2int(random.randbytes(STATE_LEN)), STATE_LEN)
        except:
            import random
            iv = int2arr8bit(random.randint(0, 2**(STATE_LEN*8) -1), STATE_LEN)
        if mode!='ECB':
            import warnings
            warnings.warn("Initail Vector is randomly selected: " + str(iv))
    else:
        assert (type(iv)==int) or (type(iv)==list)
        iv = int2arr8bit(arr8bit2int(iv), STATE_LEN)

    return keysize, mk, mod, padding, iv
    