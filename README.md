#README

Tools I have created or used to assist with my data analysis

## Copy_Images.py

Inputs: Either an array of file names or a csv of file names  
Function: Copy jpg images with given names to new directory  

## Denoise.py

Tool to take images and denoise them by non-local means denoising. Paper that describes this method can be found [here](https://www.ipol.im/pub/art/2011/bcm_nlm/article.pdf). The CV2 tool description is found [here](https://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_photo/py_non_local_means/py_non_local_means.html).  
Input: .jpg or many .jpg in a directory  
Function: Denoises image by non local means method. Smooths noisy images.  
Output: .jpg that has been denoised

## Edge_Detection.py

Attempt at using edge detection to help with networks  
Input: .jpg  
Function:Takes image and finds edges of objects within  
Output: plot of detected edges  

## FITS_Cut.py

William Waldron's Script to cutout sections of FITS files  
Input: FITS image  
Function: Takes dimension inputs and copies that area to a new FITS File  

## Grayscape.Conversion.py

Input: Images in a directory  
Function: Takes images, converts them to grayscale and saves to a new location

## Pixel_Count_inFits.py

Input: FITS image  
Function: Within a dimensional range, it gets a signal and noise values for pixels  

## Rotate_Images.py

Input: jpg images in directory  
Function: Takes images, rotates them, saves as "degree"_"file name" in new directory
