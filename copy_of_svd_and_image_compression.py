# -*- coding: utf-8 -*-
"""Copy of SVD_and_image_compression.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/11r48KQdwWHf1WqHccQNNo19o3fy0-2Y4

#**Lab 13 - Singular value decompositions and image compression**

Enter your code in the spaces provided. Do not change any of the variable names or function names that are already provided for you. In places where we specify the name of the return value, make sure that your code produces the a value with the correct name.
"""

# Do not edit this cell.

LabID="Lab13"

try:
  from graderHelp import ISGRADEPLOT
except ImportError:
  ISGRADEPLOT = True

"""**Enter your name, section number, and BYU NetID**"""

# Enter your first and last names in between the quotation marks.

first_name="Angel"

last_name="Wheelwright"

# Enter your Math 215 section number in between the quotation marks. 

section_number="1"  

# Enter your BYU NetID in between the quotation marks.  NOT YOUR BYU ID NUMBER! 

BYUNetID="aw742"

"""**Import the required packages**"""

import numpy as np
import matplotlib.pyplot as plt

"""**Problem 1**"""

# This function accepts integers m and n, and an array of singular values s and returns the Sigma matrix.

def sigma(m,n,s):
  # Put your code here.
  sigma_matrix=np.zeros((m,n))
  for i in range (len(s)):
    sigma_matrix[i,i]=s[i]
  return sigma_matrix # Put your return value here.

"""**Problem 2**"""

# This function accepts arrays u,s, and v_t, and returns the corresponing array A.

def reconstructed_array(u,s,v_t):
  # Put your code here.
  rec_array=np.matmul(u,sigma(np.shape(u)[0],np.shape(v_t)[0],s))
  rec_array=np.matmul(rec_array,v_t)
  return rec_array # Put your return value here.

"""**Problem 3**"""

# This function accepts an array A and an integer k, and returns a rank k approximation of A as computed by an SVD.

def lower_rank(A,k):
  # Put your code here.
  u,s,v_t=np.linalg.svd(A)
  u_col1=np.zeros((np.shape(u)[0],k))
  v_t_row1=np.zeros((k,np.shape(v_t)[1]))
  sigma=np.zeros((k,k))
  for i in range(np.shape(u)[0]):
    for j in range(k):
      u_col1[i,j]=u[i,j]
  for i in range(k):
    for j in range(np.shape(v_t)[1]):
      v_t_row1[i,j]=v_t[i,j]
  for i in range(k):
    sigma[i,i]=s[i]
  A_rank_k=np.matmul(u_col1,sigma)
  A_rank_k=np.matmul(A_rank_k,v_t_row1)
  return A_rank_k # Put your return value here.

"""**Downloading image data**

The simplest way to load the image into Colab is to first download it as a .png file to your local computer by clicking the link

https://drive.google.com/uc?export=download&id=1hlAEhTsqfvYX3aGFgRgFJF_gO-U5c0gH

This will allow you to download the image as a .png file.  In the top left corner of this screen you should see a little file folder icon.   Selecting it opens a new window to the left of the notebook with three tabs: "Upload", "Refresh", and "Mount Drive". Select "Upload".  This should bring up a window that allows you to select the file "Lab13Image.png" from your local machine, which will upload the file to your notebook.  You will need to do this again if you decide to close your notebook and reopen it at a later time.

**Import the image and convert it to an array**

The following cell imports the png image and creates two arrays.  The first array is a 3-dimensional array, which you can think of as three matrices, each of which describes one of three colors for the image (red, green, and blue).  The second line of the cell converts the image to grayscale, which can be represented by a single matrix, whose entries range between 0 and 1 and represent how dark or bright the corresponding pixel should be.
"""

import skimage 
from skimage import io

RGB_array = io.imread('Lab13Image.png')            
gray_array=skimage.color.rgb2gray(RGB_array)

"""The following functions can be used to display the color image and grayscale image respectively."""

def show_color(array):
  plt.figure(figsize=(10,10))
  plt.grid(None)
  plt.imshow(array)
  return None

def show_gray(array):
  plt.figure(figsize=(10,10))
  plt.grid(None)
  plt.imshow(array,cmap='gray',vmin=0,vmax=1)
  return None

""" **Problem 4**"""

# Save the value you obtain in Problem 4 as the variable original_size.
u_orig,s_orig,v_t_orig=np.linalg.svd(gray_array)
original_size=np.size(gray_array)
#len(gray_array) #np.shape(u_orig)[0]*np.shape(u_orig)[1]+np.shape(v_t_orig)[0]+np.shape(v_t_orig)[1]+len(s_orig)
original_size

"""**Problem 5**"""

# Place your plot for Problem 5 here.
plt.plot(s_orig)

"""**Problem 6**"""

# Save the value you obtain in Problem 6 as the variable min_rank.
min_rank=200

"""**Problem 7**"""

# Save the values you obtain in Problem 7 as the variables rank_100_size and relative_size.
rank_100_size=100*np.shape(u_orig)[0]+100*np.shape(v_t_orig)[1]+100
#orig_size=np.shape(u_orig)[0]*np.shape(u_orig)[1]+np.shape(v_t_orig)[0]+np.shape(v_t_orig)[1]+len(s_orig)
relative_size=rank_100_size/original_size

"""**STOP!  BEFORE YOU SUBMIT THIS LAB:**  Go to the "Runtime" menu at the top of this page, and select "Restart and run all".  If any of the cells produce error messages, you will either need to fix the error(s) or delete the code that is causing the error(s).  Then use "Restart and run all" again to see if there are any new errors.  Repeat this until no new error messages show up.

**You are not ready to submit until you are able to select "Restart and run all" without any new error messages showing up.  Your code will not be able to be graded if there are any error messages.**

To submit your lab for grading you must first download it to your compute as .py file.  In the "File" menu select "Download .py".  The resulting file can then be uploaded to http://www.math.byu.edu:30000 for grading.
"""