from setuptools import setup, find_packages

setup(
    name             = 'aes',
    version          = '1.0.0',
    description      = 'AES(Advanced Encryption Standard) in Python',
    author           = 'Donggeun Kwon',
    author_email     = 'donggeun.kwon@gmail.com',
    url              = 'https://github.com/DonggeunKwon/aes',
    download_url     = 'https://github.com/DonggeunKwon/aes/archive/1.0.tar.gz',
    install_requires = [ ],
    # packages         = find_packages(exclude = ['docs']),
    keywords         = ['AES', 'Cipher', 'Advanced Encryption Standard'],
    python_requires  = '>=3',
    classifiers      = [
        # 'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3'
    ]
)

### Build package
# python setup.py bdist_wheel
# twine upload dist/aes-1.0.0-py3-none-any.whl