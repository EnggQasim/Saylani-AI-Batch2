#!/usr/bin/env python
# coding: utf-8

# In[3]:


import matplotlib.pyplot as plt


# In[5]:


img = plt.imread('E:/Git/Numpy_04476/New folder/b.jpg')
plt.imshow(img)


# In[6]:


img1 = plt.imread('E:/Git/Numpy_04476/New folder/c.jpg')
plt.imshow(img1)


# In[7]:


Crop_img1 = img[0:500, 0:1000]
plt.imshow(Crop_img1)


# In[8]:


Crop_img2 = img1[0:500, 0:1000]
plt.imshow(Crop_img2)


# In[23]:


import numpy as np
v_Concat_Img = np.vstack((Crop_img1,Crop_img2))
plt.imshow(v_Concat_Img)


# In[24]:


import numpy as np
h_Concat_Img = np.hstack((Crop_img1,Crop_img2))
plt.imshow(h_Concat_Img)


# In[ ]:




