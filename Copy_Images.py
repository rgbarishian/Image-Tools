#This script looks at my list that I removed unwanted idexes from
#Then it copies images that match the ones remaining to a new directory
import time
import os
from shutil import copy2
import pandas as pd
import numpy as np
start_time = time.time()
"""
#Import names from csv file
#Good_Files = pd.read_csv('/home/uahstudent/Documents/Galaxy_Zoo/training_solutions_rev1_OddFeature8.csv')
Good_Files = pd.read_csv('/home/ryan/Documents/Galaxy_Zoo/30Disturbance_50Feature.csv')
#Convert to numpy array
Good_File_Names = Good_Files.iloc[:,0]
Good_File_Names = np.array(Good_File_Names)
"""
###OR###
#Import names from list
Good_File_Names = [659875,660225,660389,662371,662690,662837,664715,666760,677207,683411,684969,685559]

#Change name to x.jpg
Good_File_Names_jpg = []
for i in Good_File_Names:
    Good_File_Names_jpg.append('%s.jpg' % i) #add .jpg to end of list so its similar to file names

#Copy files with name in list to a folder within
for i in (Good_File_Names_jpg):
    for j in os.listdir('/home/ryan/Documents/Galaxy_Zoo/30Disturbance_50Feature'):#location of images we want to sort through
        if j.startswith(i):
            os.chdir('/home/ryan/Documents/Galaxy_Zoo/30Disturbance_50Feature')#May need to change this to fit wherever images are stored/coppied from
            copy2('%s' % j, '/home/ryan/Documents/Galaxy_Zoo/newhi/')#Location we want to copy images to
            #os.chdir('..')
            print(j)          
print("%s seconds" %(time.time() - start_time))
