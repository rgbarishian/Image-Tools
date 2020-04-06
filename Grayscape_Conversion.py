#Grayscale conversion done to simplify images

from PIL import Image
import os
os.chdir('..')
os.chdir('/home/ryan/Documents/Galaxy_Zoo/newhi') #chdir to location of images
names = os.listdir()
names.remove('Gray') #USED TO REMOVE A File in the list of images

for i in names:
    os.chdir('/home/ryan/Documents/Galaxy_Zoo/newhi') #chdir to location of images
    img = Image.open(i).convert('L')
    
    #Where you want to save to
    os.chdir('/home/ryan/Documents/Galaxy_Zoo/newhi/Gray')
    
    img.save(i)
    os.chdir('/home/ryan/Documents/Galaxy_Zoo/newhi') #chdir to location of images

os.chdir('/home/ryan/Documents/Astro_Software/My_Tools')

