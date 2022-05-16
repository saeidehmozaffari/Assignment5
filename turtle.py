#!/usr/bin/env python
# coding: utf-8

# In[1]:


import turtle

t = turtle.Pen()
t.shape('turtle')
x = 0
y = 0
for i in range(10):
    t.penup()
    t.setpos(x , y)
    t.pendown()
    for j in range(i+3):
        t.forward(130)
        t.left(360 / (i+3))
    x -= 1
    y -= 20
    t.penup()
    t.setpos(x , y)
    t.pendown()


# In[ ]:




