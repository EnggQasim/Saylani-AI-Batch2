#!/usr/bin/env python
# coding: utf-8

# In[20]:


import matplotlib.pyplot as plt


# In[27]:


img = plt.imread("E:/Git/Numpy_04476/a.jpg")


# In[28]:


plt.imshow(img)


# In[38]:


cropped= img[30:500, 100:500]


# In[39]:


plt.imshow(cropped)


# In[43]:


plt.imsave('E:/Git/Numpy_04476/Crop_Image.jpg', cropped)


# In[ ]:




