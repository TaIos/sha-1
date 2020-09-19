# SHA1 custom implementation

import hashlib

def sha1(data):
    m = hashlib.new("sha1")
    m.update(data)
    return m.hexdigest()
