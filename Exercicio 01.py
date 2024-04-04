#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import matplotlib.pyplot as plt

#Para sementes onde Xo = 1

x=1
x1=np.array([x])
n=6 
a=5
#c=0
m=7

for i in range(n):
    x=(a*x)%m
    x1=np.append(x1,x)
print(x1)
ind=np.arange(n+1)
plt.bar(ind, x1)
plt.show()

# Para sementes onde Xo = 4

x=4
x1=np.array([x])
n=6 # mod -1
a=5
m=7

for i in range(n):
    x=(a*x)%m
    x1=np.append(x1,x)
    
print(x1)
ind=np.arange(n+1)
plt.bar(ind, x1)
plt.show()


x=7
x1=np.array([x])
n=6 # mod -1
a=5
m=7

for i in range(n):
    x=(a*x)%m
    x1=np.append(x1,x)
    
print(x1)
ind=np.arange(n+1)
plt.bar(ind, x1)
plt.show()


# In[ ]:




