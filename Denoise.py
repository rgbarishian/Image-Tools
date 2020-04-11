import numpy as numpy
import cv2
from matplotlib import pyplot as plt
import os

os.chdir('Test_Images/')
files = os.listdir()



# # img = cv2.imread('Test_Images/90_664374.jpg')
# # img = cv2.imread('Test_Images/90_Webp.net-resizeimage.jpg')
# img = cv2.imread('Test_Images/90_123938.jpg')

# dst = cv2.fastNlMeansDenoising(img, None, 10,10,7)
# thirtyseventwentyone = cv2.fastNlMeansDenoising(img, None,15,7,21)

# # Plotting of source and destination image 
# plt.subplot(131), plt.imshow(img) 
# plt.subplot(132), plt.imshow(dst)
# plt.subplot(133), plt.imshow(thirtyseventwentyone)
  
# plt.show() 

for i in files:
    img = cv2.imread(i)
    dst = cv2.fastNlMeansDenoising(img, None, 10,10,7)
    thirtyseventwentyone = cv2.fastNlMeansDenoising(img, None,15,9,21)

    cv2.imwrite('Filtered/'+i, dst)