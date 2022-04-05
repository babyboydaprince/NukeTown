from hashlib import md5
from string import ascii_letters


# Get sugar numbers
def getSugarByKey(key, message):
    sugar = ''
    yHash = md5(key.Encode()).hexdigest()

    while True:
        for char in yHash:
            if len(sugar) == len(message):
                break
            if char not in ascii_letters:
                sugar += char

        if len(sugar) == len(message):
            return sugar
