# -*- coding: utf-8 -*-
import sys


def int2arr8bit(Int:int, arr_size:int) -> list:
    if type(Int)==list: return Int
    if arr_size==0: return []
    # check it is a value
    assert type(Int)==int, "check input type"

    arr = []

    for i in range(arr_size):
        arr.append((Int >> (8 * (arr_size - 1 - i))) & 0xFF)

    if ((Int >> (8 * (arr_size))) & 0xFF):
        import warnings
        warnings.warn("data lost, input: " + str(arr_size) + " / lost: " + str((Int >> (8 * (arr_size)))))

    return arr

def arr8bit2int(arr:list) -> int:
    if type(arr)==int: return arr
    # check it is a value
    assert type(arr)==list, "check input type"

    ints = 0
    for i in range(len(arr)):
        ints += arr[len(arr) - 1 - i] * (0x100**i)

    return ints

def bytes2int(Bytes:bytes) -> int:
    if type(Bytes)==int: return Bytes
    # check it is a value
    assert type(Bytes)==bytes, "check input type"
    
    Ints = int.from_bytes(Bytes, byteorder=sys.byteorder)

    return Ints

def int2bytes(Int:int, size:int=None) -> bytes:
    if type(Int)==bytes: return Int
    # check it is a value
    assert type(Int)==int, "check input type"

    if size is None:
        length = len(bin(Int)[2:])
        size = (length // 8) + int(length % 8 > 0)
    Bytes = (Int).to_bytes(size, byteorder=sys.byteorder)

    return Bytes

def str2int(String, encode_type='utf-8'):
    Int = bytes2int(String.encode(encode_type))

    return Int

def int2str(Int, encode_type='utf-8'):
    Bytes = int2bytes(Int)
    String = Bytes.decode(encoding=encode_type)

    return String

def str2arr8bit(String, encode_type='utf-8'):
    Bytes = String.encode(encode_type)
    length = len(Bytes)
    Int = bytes2int(String.encode(encode_type))
    arr = int2arr8bit(Int, length)

    return arr

