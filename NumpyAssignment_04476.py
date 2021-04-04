#!/usr/bin/env python
# coding: utf-8

# # Task 1: Image cropping (500 * 500)

# In[1]:


import numpy as np
import matplotlib.pyplot as plt


# In[2]:


img = plt.imread("E:/Python/Numpy_04476/Numpy_04476/a.jpg")
plt.imshow(img)


# In[7]:


height , width = img.shape[:2]


# In[12]:


h = height/2
w = width/2
print(h)
print(w)


# In[13]:


Crop_image = img[int(h)-250:int(h)+250, int(w)-250:int(w)+250]


# In[14]:


plt.imshow(Crop_image)


# # Task 2: Merge Image Horizontally & Vertically

# In[18]:


img = plt.imread('E:/Python/Numpy_04476/Numpy_04476/New folder/b.jpg')
plt.imshow(img)


# In[19]:



img1 = plt.imread('E:/Python/Numpy_04476/Numpy_04476/New folder/c.jpg')
plt.imshow(img1)


# In[20]:


Crop_img1 = img[0:500, 0:1000]
plt.imshow(Crop_img1)


# In[21]:



Crop_img2 = img1[0:500, 0:1000]
plt.imshow(Crop_img2)


# ### Vertically Merge

# In[22]:


v_Concat_Img = np.vstack((Crop_img1,Crop_img2))
plt.imshow(v_Concat_Img)


# ### Horizontally Merge 

# In[23]:


h_Concat_Img = np.hstack((Crop_img1,Crop_img2))
plt.imshow(h_Concat_Img)


# # Task 3: Convert RGB image into Grayscale

# In[25]:


Color_img = plt.imread('E:/Python/Numpy_04476/Numpy_04476/a.jpg')
plt.imshow(Color_img)


# In[26]:


R, G, B = Color_img[:,:,0], Color_img[:,:,1],Color_img[:,:,2]


# In[27]:


Y = 0.299*R+0.587*G+0.114*B


# In[28]:


plt.imshow(Y, cmap='gray')


# # Task 4: Apply Filter on Image

# In[29]:


Color_img = plt.imread('E:/Python/Numpy_04476/Numpy_04476/a.jpg')
plt.imshow(Color_img)


# In[30]:


def convolve(image, filter, padding = (1, 1)):
    # For this to work neatly, filter and image should have the same number of channels
    # Alternatively, filter could have just 1 channel or 2 dimensions
    
    if(image.ndim == 2):
        image = np.expand_dims(image, axis=-1) # Convert 2D grayscale images to 3D
    if(filter.ndim == 2):
        filter = np.repeat(np.expand_dims(filter, axis=-1), image.shape[-1], axis=-1) # Same with filters
    if(filter.shape[-1] == 1):
        filter = np.repeat(filter, image.shape[-1], axis=-1) # Give filter the same channel count as the image
    
    #print(filter.shape, image.shape)
    assert image.shape[-1] == filter.shape[-1]
    size_x, size_y = filter.shape[:2]
    width, height = image.shape[:2]
    
    output_array = np.zeros(((width - size_x + 2*padding[0]) + 1, 
                             (height - size_y + 2*padding[1]) + 1,
                             image.shape[-1])) # Convolution Output: [(W−K+2P)/S]+1
    
    padded_image = np.pad(image, [
        (padding[0], padding[0]),
        (padding[1], padding[1]),
        (0, 0)
    ])
    
    for x in range(padded_image.shape[0] - size_x + 1): # -size_x + 1 is to keep the window within the bounds of the image
        for y in range(padded_image.shape[1] - size_y + 1):

            # Creates the window with the same size as the filter
            window = padded_image[x:x + size_x, y:y + size_y]

            # Sums over the product of the filter and the window
            output_values = np.sum(filter * window, axis=(0, 1)) 

            # Places the calculated value into the output_array
            output_array[x, y] = output_values
            
    return output_array


# In[39]:


from PIL import Image
filter = np.array([
    [-1, 0, 1],
    [-1, 0, 1],
    [-1, 0, 1]
], dtype=np.float32)/9.0 # Box Filter

image = Color_img
image_arr = np.array(image)/255.0

convolved_arr = convolve(image_arr, filter, padding=(1, 1))
convolved = Image.fromarray(np.uint8(255 * convolved_arr), 'RGB') # Convolved Image
plt.imshow(convolved)
plt.show()


# # Task 5: Image Rotation

# In[34]:


from PIL import Image
import math




# In[35]:


image = np.array(Color_img)
angle=int(input("Enter the angle :- "))

# Define the most occuring variables
angle=math.radians(angle)                               #converting degrees to radians
cosine=math.cos(angle)
sine=math.sin(angle)
height=image.shape[0]                                   #define the height of the image
width=image.shape[1]                                    #define the width of the image

# Define the height and width of the new image that is to be formed
new_height  = round(abs(image.shape[0]*cosine)+abs(image.shape[1]*sine))+1
new_width  = round(abs(image.shape[1]*cosine)+abs(image.shape[0]*sine))+1

# define another image variable of dimensions of new_height and new _column filled with zeros
output=np.zeros((new_height,new_width,image.shape[2]))

# Find the centre of the image about which we have to rotate the image
original_centre_height   = round(((image.shape[0]+1)/2)-1)    #with respect to the original image
original_centre_width    = round(((image.shape[1]+1)/2)-1)    #with respect to the original image

# Find the centre of the new image that will be obtained
new_centre_height= round(((new_height+1)/2)-1)        #with respect to the new image
new_centre_width= round(((new_width+1)/2)-1)          #with respect to the new image

for i in range(height):
    for j in range(width):
        #co-ordinates of pixel with respect to the centre of original image
        y=image.shape[0]-1-i-original_centre_height                   
        x=image.shape[1]-1-j-original_centre_width                      

        #co-ordinate of pixel with respect to the rotated image
        new_y=round(-x*sine+y*cosine)
        new_x=round(x*cosine+y*sine)

        '''since image will be rotated the centre will change too, 
           so to adust to that we will need to change new_x and new_y with respect to the new centre'''
        new_y=new_centre_height-new_y
        new_x=new_centre_width-new_x

        # adding if check to prevent any errors in the processing
        if 0 <= new_x < new_width and 0 <= new_y < new_height and new_x>=0 and new_y>=0:
            output[new_y,new_x,:]=image[i,j,:]                          #writing the pixels to the new destination in the output image

pil_img=Image.fromarray((output).astype(np.uint8))                       # converting array to image
#pil_img.save("rotated_image.png") 
plt.imshow(pil_img)


# In[ ]:




