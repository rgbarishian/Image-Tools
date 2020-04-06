from PIL import Image
import os

os.chdir('/home/ryan/Documents/Galaxy_Zoo/newhi')
names = os.listdir()
names.remove('Gray') #USED TO REMOVE A File in the list of images
names.remove('rotate')
for i in names:
    os.chdir('/home/ryan/Documents/Galaxy_Zoo/newhi') #chdir to location of images
    img = Image.open(i).rotate(180) #90,180,270
    
    
    #Where you want to save to
    os.chdir('/home/ryan/Documents/Galaxy_Zoo/newhi/rotate')
    
    img.save(i)
    os.rename('%s' % i, '180_%s' % i)
    #os.chdir('/home/ryan/Documents/Galaxy_Zoo/newhi') #chdir to location of images

os.chdir('/home/ryan/Documents/Astro_Software/My_Tools')