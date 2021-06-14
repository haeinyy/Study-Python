#!/usr/bin/env python
# coding: utf-8

# In[5]:


# mod2.py 
PI = 3.141592

class Math:
    # 원넓이
    def solv(self, r):
        return PI * (r**2)
    
def add(a,b):
    return a+b


# In[6]:


if __name__ == "__main__":
    a = Math()
    print(a.solv(2))

