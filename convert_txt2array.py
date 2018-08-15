mport os
import numpy as np
import pandas as pd

#mergefiledir=os.getcwd()+'/MergeTXT/testTXT/'
#filenames=os.listdir(mergefiledir)
#f=open('test2.txt','w')
#line=f.readline()
#a=np.genfromtxt('test_imagenames.txt')


file = open ("test_imagenames.txt", "r")
x = []
for item in file:
        x.append(item.split ('\s')) # Process the item here if you wish before appending
        a = np.array(x)
        print(a[:1]) #print the first row
        print(a[1:]) #print the first colum
