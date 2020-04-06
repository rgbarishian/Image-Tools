from astropy.io import fits
from astropy.utils.data import get_pkg_data_filename
import numpy as np
import math
import csv
#import image
image = fits.open('/home/ryan/Documents/Galaxy_Zoo/22.fits') #fits file
signal = image[1].data
x = image[1].header['NAXIS2']
y = image[1].header['NAXIS1']

#get signals for all points
x = 2000#for testing purposes
y = 1500# for tsting purposes

signals = []
noise = []
x_list = []
y_list = []
for i in range (0,x):
    for j in range (0,y):
        #print(signal[i,j])
        if signal[i,j] == 0:
            continue
        else:
            signals.append(signal[i,j]) #create list of signal
            x_list.append(i) #list of points on x axis
            y_list.append(j) # list of point of y axis
            noise.append(math.sqrt(signal[i,j]))

#boolean mask


#Prep and print 3 docs to list
zip(x_list,y_list, signals, noise)
with open('/home/ryan/Documents/sources.reg', 'w') as fid:
    writer = csv.writer(fid, delimiter='\t')
    writer.writerows(zip(x_list,y_list, signals, noise))