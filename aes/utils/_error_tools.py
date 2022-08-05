# -*- coding: utf-8 -*-

class KeysizeError(Exception):
    def __init__(self, msg:str=""):
        super().__init__("Invalid key size: "+str(msg))

class KeyvalueError(Exception):
    def __init__(self, msg:str=""):
        super().__init__("Input key value doesn't match with input key size: "+str(msg))

class ModeofOperationError(Exception):
    def __init__(self, msg:str=""):
        super().__init__("Invalid mode of operation: "+str(msg))

class PaddingError(Exception):
    def __init__(self, msg:str=""):
        super().__init__("Invalid padding method: "+str(msg))

class CustomError(Exception):
    def __init__(self, msg:str=""):
        super().__init__("Custom Error: "+str(msg))
