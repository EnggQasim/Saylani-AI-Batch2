#!/usr/bin/env python
# coding: utf-8

# In[3]:


import numpy as np
import matplotlib.pyplot as plt


# In[4]:


Color_img = plt.imread('E:/Git/Numpy_04476/a.jpg')


# In[6]:


plt.imshow(Color_img)


# In[61]:


R, G, B = Color_img[:,:,0], Color_img[:,:,1],Color_img[:,:,2]
#print(R, G, B)


# In[62]:


Y = 0.299*R+0.587*G+0.114*B
#Y


# In[60]:


plt.imshow(Y, cmap='gray')


# In[ ]:





# In[ ]:




