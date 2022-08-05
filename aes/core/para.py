# -*- coding: utf-8 -*-

### parameters ###
STATE_SIZE = 16
STATE_LEN = STATE_SIZE

KEY_SIZE_LIST = [128, 192, 256]

MODE_OF_OPERATION_LIST = ['ECB', 'CBC', 'CTR'] # 'CFB', 'OFB'

PADDING_LIST = ['PKCS#7', 'byte'] # bit, ANSI X9.23, ISO 10126


### Test Vector ###
TEST_VECTOR_KEY_EXPANSION_128 = [0x2b, 0x7e, 0x15, 0x16, 0x28, 0xae, 0xd2, 0xa6, 0xab, 0xf7, 0x15, 0x88, 0x09, 0xcf, 0x4f, 0x3c]
TEST_VECTOR_KEY_EXPANSION_192 = [0x8e, 0x73, 0xb0, 0xf7, 0xda, 0x0e, 0x64, 0x52, 0xc8, 0x10, 0xf3, 0x2b,
                                 0x80, 0x90, 0x79, 0xe5, 0x62, 0xf8, 0xea, 0xd2, 0x52, 0x2c, 0x6b, 0x7b]
TEST_VECTOR_KEY_EXPANSION_256 = [0x60, 0x3d, 0xeb, 0x10, 0x15, 0xca, 0x71, 0xbe, 0x2b, 0x73, 0xae, 0xf0, 0x85, 0x7d, 0x77, 0x81,
                                 0x1f, 0x35, 0x2c, 0x07, 0x3b, 0x61, 0x08, 0xd7, 0x2d, 0x98, 0x10, 0xa3, 0x09, 0x14, 0xdf, 0xf4]

'''
import aes

TEST_VECTOR_PLAIN_128  = aes.utils.int2arr8bit(0x00112233445566778899aabbccddeeff, 16)
TEST_VECTOR_KEY_128    = aes.utils.int2arr8bit(0x000102030405060708090a0b0c0d0e0f, 16)
TEST_VECTOR_CIPHER_128 = aes.utils.int2arr8bit(0x69c4e0d86a7b0430d8cdb78070b4c55a, 16)


TEST_VECTOR_PLAIN_192  = aes.utils.int2arr8bit(0x00112233445566778899aabbccddeeff, 16)
TEST_VECTOR_KEY_192    = aes.utils.int2arr8bit(0x000102030405060708090a0b0c0d0e0f1011121314151617, 24)
TEST_VECTOR_CIPHER_192 = aes.utils.int2arr8bit(0xdda97ca4864cdfe06eaf70a0ec0d7191, 16)

TEST_VECTOR_PLAIN_256  = aes.utils.int2arr8bit(0x00112233445566778899aabbccddeeff, 16)
TEST_VECTOR_KEY_256    = aes.utils.int2arr8bit(0x000102030405060708090a0b0c0d0e0f101112131415161718191a1b1c1d1e1f, 32)
TEST_VECTOR_CIPHER_256 = aes.utils.int2arr8bit(0x8ea2b7ca516745bfeafc49904b496089, 16)

rk = aes.core.key_expansion(TEST_VECTOR_KEY_128, 128)
ct = aes.core.encryption(TEST_VECTOR_PLAIN_128, rk)
print(ct == TEST_VECTOR_CIPHER_128)
pt = aes.core.decryption(ct, aes.core.key_expansion(TEST_VECTOR_KEY_128, 128))
print(pt == TEST_VECTOR_PLAIN_128)

rk = aes.core.key_expansion(TEST_VECTOR_KEY_192, 192)
ct = aes.core.encryption(TEST_VECTOR_PLAIN_192, rk)
print(ct == TEST_VECTOR_CIPHER_192)
pt = aes.core.decryption(ct, aes.core.key_expansion(TEST_VECTOR_KEY_192, 192))
print(pt == TEST_VECTOR_PLAIN_192)

rk = aes.core.key_expansion(TEST_VECTOR_KEY_256, 256)
ct = aes.core.encryption(TEST_VECTOR_PLAIN_256, rk)
print(ct == TEST_VECTOR_CIPHER_256)
pt = aes.core.decryption(ct, aes.core.key_expansion(TEST_VECTOR_KEY_256, 256))
print(pt == TEST_VECTOR_PLAIN_256)
'''