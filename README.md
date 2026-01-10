# AES - Advanced Encryption Standard

[![PyPI](https://img.shields.io/pypi/v/aes)](https://pypi.org/project/aes/)
[![Downloads](https://pepy.tech/badge/aes)](https://pypi.org/project/aes/)
[![GitHub](https://img.shields.io/github/license/donggeunkwon/aes)](https://github.com/donggeunkwon/aes/blob/master/LICENSE)

A simple and easy-to-use Python package for Advanced Encryption Standard (AES) Block Cipher [[FIPS 197 PDF](http://csrc.nist.gov/publications/fips/fips197/fips-197.pdf)]

## 📋 Table of Contents

- [Features](#features)
- [Installation](#installation)
- [Quick Start](#quick-start)
- [Usage Examples](#usage-examples)
  - [Basic Encryption/Decryption](#basic-encryptiondecryption)
  - [Using Core Functions](#using-core-functions)
  - [Modes of Operation](#modes-of-operation)
- [API Reference](#api-reference)
- [Security Considerations](#security-considerations)
- [Version History](#version-history)
- [Contributing](#contributing)
- [License](#license)

## ✨ Features

Version 1.2.0 is now available with extended support!

| Feature | Support |
|---------|---------|
| **Key Sizes** | AES-128, AES-192, AES-256 |
| **Modes of Operation** | ECB, CBC, CTR |
| **Padding Schemes** | PKCS#7 |
| **Input Format** | Integer, Byte Arrays |
| **Core Functions** | Encryption, Decryption, Key Expansion |

## 📦 Installation

Install the package from PyPI using pip:

```bash
pip install aes
```

### Verify Installation

After installation, verify that the package is working correctly:

```python
from aes import aes

# Create a simple cipher instance
cipher = aes(0)

# Test encryption and decryption
result = cipher.dec_once(cipher.enc_once(0))
print(result)
# Expected output: [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
```

If you see a list of zeros, the installation was successful!

## 🚀 Quick Start

### Basic Usage (Without Mode of Operation)

For simple encryption/decryption without a specific mode of operation, use `enc_once` and `dec_once`:
```python
import aes

# Define master key and plaintext
master_key = 0x000102030405060708090a0b0c0d0e0f
plaintext = 0x00112233445566778899aabbccddeeff

# Create AES-128 cipher instance
cipher = aes.aes(master_key, 128)

# Encrypt
ciphertext = cipher.enc_once(plaintext)
print(f"Ciphertext (array): {ciphertext}")
print(f"Ciphertext (hex): 0x{hex(aes.utils.arr8bit2int(ciphertext))[2:].zfill(32)}")
# Output: 0x69c4e0d86a7b0430d8cdb78070b4c55a

# Decrypt
recovered = cipher.dec_once(ciphertext)
print(f"Recovered (array): {recovered}")
print(f"Recovered (hex): 0x{hex(aes.utils.arr8bit2int(recovered))[2:].zfill(32)}")
# Output: 0x00112233445566778899aabbccddeeff
```

## 📚 Usage Examples

### Basic Encryption/Decryption

#### AES-128 Example

```python
import aes

# 128-bit key and plaintext
key = 0x000102030405060708090a0b0c0d0e0f
plaintext = 0x00112233445566778899aabbccddeeff

# Create cipher
cipher = aes.aes(key, 128)

# Encrypt and decrypt
ciphertext = cipher.enc_once(plaintext)
recovered = cipher.dec_once(ciphertext)

assert aes.utils.arr8bit2int(recovered) == plaintext
```

### Using Core Functions

If you want direct access to the core AES functions:
```python
import aes

# Convert integers to byte arrays
master_key = 0x000102030405060708090a0b0c0d0e0f
plaintext = 0x000102030405060708090a0b0c0d0e0f

mk_arr = aes.utils.int2arr8bit(master_key, 16)
pt_arr = aes.utils.int2arr8bit(plaintext, 16)

# Key expansion
round_keys = aes.core.key_expansion(mk_arr, 128)

# Core encryption
ct_arr = aes.core.encryption(pt_arr, round_keys)
print(f"Ciphertext: 0x{hex(aes.utils.arr8bit2int(ct_arr))[2:].zfill(32)}")
# Output: 0x0a940bb5416ef045f1c39458c653ea5a

# Core decryption
pr_arr = aes.core.decryption(ct_arr, round_keys)
print(f"Recovered: 0x{hex(aes.utils.arr8bit2int(pr_arr))[2:].zfill(32)}")
# Output: 0x000102030405060708090a0b0c0d0e0f
```

### Modes of Operation

#### CTR Mode with AES-256
```python
import aes

# 256-bit key
master_key = 0x000102030405060708090a0b0c0d0e0f101112131415161718191a1b1c1d1e1f
plaintext = 0x00112233445566778899aabbccddeeff

# Convert to byte arrays
pt_arr = aes.utils.int2arr8bit(plaintext, 16)

# Create cipher with CTR mode and PKCS#7 padding
cipher = aes.aes(master_key, 256, mode='CTR', padding='PKCS#7')

# Encrypt (note: enc/dec methods work with byte arrays)
ct_arr = cipher.enc(pt_arr)
print(f"Ciphertext: 0x{hex(aes.utils.arr8bit2int(ct_arr))[2:].zfill(32)}")

# Decrypt
pr_arr = cipher.dec(ct_arr)
print(f"Recovered: 0x{hex(aes.utils.arr8bit2int(pr_arr))[2:].zfill(32)}")
# Output: 0x00112233445566778899aabbccddeeff
```

#### Important: Initialization Vector (IV)

When using CBC or CTR modes without specifying an IV, a random one will be generated:

```python
cipher = aes.aes(key, 256, mode='CBC')
# Warning: Initial Vector is randomly selected: [23, 202, 118, 211, ...]
```

**Always save the IV for decryption:**

```python
# Save the IV
iv = cipher.iv
print(f"IV: {iv}")  # Save this for later decryption!

# For decryption with the same IV
cipher_decrypt = aes.aes(key, 256, mode='CBC', iv=iv)
```

#### CBC Mode Example

```python
import aes

key = 0x000102030405060708090a0b0c0d0e0f
plaintext_arr = aes.utils.int2arr8bit(0x00112233445566778899aabbccddeeff, 16)

# Specify custom IV (recommended)
custom_iv = [0] * 16

cipher = aes.aes(key, 128, mode='CBC', iv=custom_iv, padding='PKCS#7')
ciphertext = cipher.enc(plaintext_arr)
recovered = cipher.dec(ciphertext)
```

## 📖 API Reference

### Class: `aes.aes`

Create an AES cipher instance.

```python
cipher = aes.aes(key, key_size=128, mode=None, iv=None, padding=None)
```

**Parameters:**

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `key` | int or list | required | Master key (integer or byte array) |
| `key_size` | int | 128 | Key size in bits (128, 192, or 256) |
| `mode` | str | None | Mode of operation ('ECB', 'CBC', 'CTR') |
| `iv` | list | None | Initialization vector (required for CBC/CTR) |
| `padding` | str | None | Padding scheme ('PKCS#7') |

**Methods:**

- `enc_once(plaintext)` - Encrypt a single block (no mode)
- `dec_once(ciphertext)` - Decrypt a single block (no mode)
- `enc(plaintext_array)` - Encrypt with mode of operation
- `dec(ciphertext_array)` - Decrypt with mode of operation

### Core Functions

```python
# Key expansion
round_keys = aes.core.key_expansion(key_array, key_size)

# Block encryption/decryption
ciphertext = aes.core.encryption(plaintext_array, round_keys)
plaintext = aes.core.decryption(ciphertext_array, round_keys)
```

### Utility Functions

```python
# Convert integer to byte array
byte_array = aes.utils.int2arr8bit(integer_value, byte_length)

# Convert byte array to integer
integer_value = aes.utils.arr8bit2int(byte_array)
```

## 🔒 Security Considerations

1. **Never hardcode keys**: Store keys securely using environment variables or key management systems
2. **Use random IVs**: For CBC and CTR modes, always use a cryptographically secure random IV
3. **Key size**: Use AES-256 for sensitive data requiring long-term security
4. **Mode selection**:
   - **ECB**: Not recommended (no IV, patterns visible in ciphertext)
   - **CBC**: Good for general purpose, requires random IV
   - **CTR**: Excellent for parallel processing, requires unique IV/nonce
5. **Authentication**: AES only provides confidentiality. Use HMAC or authenticated encryption (GCM) for integrity
6. **Padding oracle attacks**: Be aware when using CBC with PKCS#7 padding

## 📋 Version History

| Version | Release Date | Changes |
|---------|--------------|---------|
| **v1.2.0** | Latest | Added AES-192, AES-256 support<br>Added CBC and CTR modes<br>Improved API design |
| **v1.0.1** | - | Fixed `ModuleNotFoundError` bug |
| **v1.0.0** | - | Initial release with AES-128 support |

## 🤝 Contributing

Contributions are welcome! If you'd like to contribute:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

### Reporting Bugs

If you find a bug, please open an issue on GitHub or contact:

**Donggeun Kwon** - donggeun.kwon@gmail.com

## 📄 License

This project is licensed under the terms specified in the [LICENSE](https://github.com/donggeunkwon/aes/blob/master/LICENSE) file.

## 🔗 Resources

- [FIPS 197 - AES Specification](http://csrc.nist.gov/publications/fips/fips197/fips-197.pdf)
- [PyPI Package](https://pypi.org/project/aes/)
- [GitHub Repository](https://github.com/donggeunkwon/aes)

---

Made with ❤️ by [Donggeun Kwon](https://github.com/donggeunkwon)
