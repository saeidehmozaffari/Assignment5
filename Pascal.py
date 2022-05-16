#!/usr/bin/env python
# coding: utf-8

# In[1]:


def pascal(n):
    khayam=[[0 for i in range(n)]for j in range(n)]
    for i in range(n):
        khayam[i][0]=1
        khayam[i][i]=1
    for i in range(2,n):
        for j in range(1,i):
            khayam[i][j]=khayam[i-1][j]+khayam[i-1][j-1]
    for i in range(n):
        for j in range(i+1):
            print(khayam[i][j],end=' ')
        print ()
x=int(input())
pascal(x)


# In[ ]:




