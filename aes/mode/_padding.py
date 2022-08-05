# -*- coding: utf-8 -*-

def byte_padding(data, block_size, unpad=False, inv=False):
    d = data.copy()
    
    if not unpad:
        pad = block_size - len(data)
        while(len(d)<block_size-1):
            if inv:
                d = d + [0]
            else:
                d = [0] + d
        
        if inv:
            d = d + [pad]
        else:
            d = [pad] + d
    
    else:
        if inv:
            pad = d[-1]
            d = d[:-pad]
        else:
            pad = d[0]
            d = d[pad:]

    return d

def pkcs_padding(data, block_size, unpad=False, inv=False):
    d = data.copy()
    
    if not unpad:
        pad = block_size - len(data)
        while(len(d)<block_size):
            if inv:
                d = d + [pad]
            else:
                d = [pad] + d
    else:
        if inv:
            pad = d[-1]
            d = d[:-pad]
        else:
            pad = d[0]
            d = d[pad:]
    
    return d