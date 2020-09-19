import hashlib
import string 
import random
from impl import sha1

def test_hashlib():
    for N in range(1000): # data length
        for i in range(5): # repeat for each length
            data = ''.join(random.choices(string.ascii_uppercase +
                                 string.digits, k = N)).encode('utf-8')
            m = hashlib.new("sha1")
            m.update(data)
            assert sha1(data) == m.hexdigest() 
