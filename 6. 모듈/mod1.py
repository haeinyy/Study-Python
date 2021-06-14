#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Mod1.py
def add(a,b):
    return a+b

def sub(a,b):
    return a-b


# In[4]:


# 직접 이 파일은 실행 할 때, 아래 구문 실행
# 하지만, 다른 파일에서 이 모듈을 import해서 사용하면..?? => 실행안됨
if __name__ == '__main__':
    print(add(1,4))
    print(sub(1,4))

