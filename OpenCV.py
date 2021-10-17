#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Importing packages.

import cv2 as cv    
import matplotlib.image as mpimg
import os                                             
import sys
import numpy
import matplotlib.pyplot as plt


# In[6]:


#REading the image  Cat from the directory.
img = mpimg.imread(os.path.join(os.getcwd(),"Pictures\Camera Roll\cat.jpg"))


# In[23]:


#Displaying the above read image using cv.
cv.imshow('cat',img)


# In[7]:


#Reading the image Dog from the directory
img2=mpimg.imread(os.path.join(os.getcwd(),"Pictures\Camera Roll\dog.jpg"))


# In[7]:


#Displaying the above read image using cv.
cv.imshow('dog',img2)


# In[12]:


#Displaying the Cat image using matplotlib.
plt.imshow(img)


# In[10]:


#Displaying the Dog image using cv.
plt.imshow(img2)


# In[19]:


print(img)   #Printing the image matrix of Cat


# In[16]:


numpy.set_printoptions(threshold=sys.maxsize) # This changes the print option to display the entire matrix without truncation.


# In[15]:


R,G,B = cv.split(img)   #This split the image Cat into its respective RGB channels.
print(img.shape)   #This displays the dimensions of the above spilt image matrix.


# In[14]:


print(R)    #This is the split Red channel of the image Cat in the form of matrix.


# In[17]:


print(G)    #This is the split Green channel of the image Cat in the form of matrix.


# In[18]:


print(B)    #This is the split Blue channel of the image Cat in the form of matrix.


# In[13]:


plt.imshow(R,cmap='Reds')  #This is the split Red channel of the image Cat in the form of an image.


# In[14]:


plt.imshow(G,cmap='Greens')  #This is the split Green channel of the image Cat in the form of an image.


# In[16]:


plt.imshow(B,cmap='Blues')   #This is the split Blue channel of the image Cat in the form of an image.


# In[28]:


img3=mpimg.imread(os.path.join(os.getcwd(),"Pictures\Camera Roll\image.jpg"))


# In[29]:


R,G,B = cv.split(img3)


# In[30]:


plt.imshow(G,cmap='Greens')


# In[31]:


plt.imshow(B,cmap='Blues')


# In[32]:


plt.imshow(R,cmap='Reds')


# In[22]:


imgGray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)  #Saving the converted Coloured Cat image to GrayScale image in imgGray.
print(imgGray)                                #Printing the converted GrayScale image in the form of matrix.


# In[24]:


plt.imshow(imgGray,cmap='gray')                   #Printing the converted GrayScale image in the form of an image.

