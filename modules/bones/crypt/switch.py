from base64 import b64encode
from base64 import b64decode

# Switch


def switch(text, key):
    out = ''
    for i in range(len(text)):
        current = text[i]
        current_key = key[i % len(key)]
        out += chr(ord(current) ^ ord(current_key))
    return out

# Encode : [text => switch base64]


def encode(text, key):
    return b64encode(switch(text, key).encode('utf-8')).decode()

# Decode : [switch => base64 => text]


def decode(text, key):
    return switch(b64decode(text).decode(), key)
