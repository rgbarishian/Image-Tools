#!/usr/bin/env python
# coding: utf-8
#From william waldron
# # Making/Saving a FITS Cutout
# 
# This notebook is to give a simple example of how to make a FITS file cutout. This assumes that the original WCS does not need to be retained although there are ways to keep that information too.
# 
# Generally, when making a cutout of a FITS image in Python, one only needs to index like a numpy array which will return the image as an array. However, it is possible to retain the WCS information with [Cutout2D](https://docs.astropy.org/en/stable/api/astropy.nddata.utils.Cutout2D.html).

# In[40]:


# Python Imports
from warnings import catch_warnings, simplefilter

# 3rd Party Imports
from matplotlib import pyplot as plt
from skimage import img_as_ubyte
from skimage.io import imsave

# Astropy Imports
from astropy.io import fits
from astropy.wcs import WCS
from astropy.utils import data as astrodata
from astropy.nddata.utils import Cutout2D
from astropy.visualization import LinearStretch, PercentileInterval, ImageNormalize


# ## Read in the Data
# 
# A standard piece to any pipeline is reading in the data. We will use a built in Astropy example file to demonstrate.

# In[13]:


# Read in the Data
fileName = astrodata.get_pkg_data_filename('/home/ryan/Documents/Astro_Software/My_Tools/CutOutExample/Cutout1.fits')
with fits.open(fileName) as fid:
    img = {
        'data': fid[0].data,
        'header': fid[0].header,
        'wcs': WCS(fid[0])
    }


# ## Plot the Data

# In[21]:


# Create the Figure
fig = plt.figure(figsize=(10, 7))
ax = fig.add_subplot(1, 1, 1, projection=img['wcs'])
fig.add_axes(ax)
norm = ImageNormalize(img['data'], PercentileInterval(99.9), stretch=LinearStretch())

# Add the Image
im = ax.imshow(img['data'], norm=norm, origin='lower', cmap='gray')

# Add the Colorbar
cb = fig.colorbar(im, ax=ax)
cb.set_label('Counts')


# ## Creating an Image Cutout as Another Format
# 
# This section saves a cutout of the image above as a PNG file.

# In[46]:


# Get the Cutout
cut = img['data'][300:650, 300:700]  # Index Range Desired
cut = cut.astype('uint16')  # Only had to do this for this img type

# # Convert to 8-bit if desired
# with catch_warnings():
#     simplefilter('ignore')
#     cut = img_as_ubyte(cut)  # Only if 8 bit png guarunteed

# Plot the Cut
fig, ax = plt.subplots()
ax.imshow(cut, origin='lower', norm=norm, cmap='gray')

# Save the Cutout as PNG
imsave('Cutout2.png', cut)


# ## Creating an Image Cutout as a FITS
# 
# This section saves a cutout of the image above as a FITS file.

# In[52]:


# Get the Cutout
cut = Cutout2D(img['data'], (500, 475), (350, 400), wcs=img['wcs'])

# Plot the Cut
fig = plt.figure()
ax = fig.add_subplot(1, 1, 1, projection=cut.wcs)
fig.add_axes(ax)
ax.imshow(cut.data, origin='lower', norm=norm, cmap='gray')

# Make the HDU List
hdus = fits.HDUList()

# Add a Primary Header
hdu = fits.PrimaryHDU()
hdu.header.add_comment('A Cutout of the Horse Head Nebula')
hdu.header.add_comment('Author: Will Waldron')
hdus.append(hdu)

# Add the Image Header
hdu = fits.ImageHDU(cut.data, cut.wcs.to_header(), 'SCI')
hdus.append(hdu)

# Save the Image
hdus.writeto('/home/ryan/Documents/Astro_Software/My_Tools/Cutout2.fits', overwrite=True)

