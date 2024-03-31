def data_types():
    srh = input()
    if(srh == "Long"):
        return 8
    elif(srh == "Integer"):
        return 4
    elif(srh == "Float"):
        return 4
    elif(srh == "Double"):
        return 8
    elif(srh == "Character"):
        return 1
    else:
        return 0
print(data_types())


from typing import *

def dataTypes(type: str) -> int:
    """
    Returns the size in bytes of the given data type.
    """
    data_types = {
        "Integer": 4,
        "Long": 8,
        "Float": 4,
        "Double": 8,
        "Character": 1
    }

    if type in data_types:
        return data_types[type]
    else:
        return -1

# Test cases
 # Output: -1



##    Integer: 4 bytes
##Long: 8 bytes
##Float: 4 bytes
##Double: 8 bytes
##Character: 1 byte
