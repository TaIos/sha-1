#!/usr/bin/env python
# coding: utf-8

# In[5]:


import hashlib

def sha1(data):
    m = hashlib.new("sha1")
    m.update(data)
    return m.hexdigest()

