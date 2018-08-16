import sys
import glob
import os
import cv2
#usage
# python image_flip.py src_path tar_path
src_path = sys.argv[1]
tar_path = sys.argv[2]
if not os.path.exists(tar_path):
        os.makedirs(tar_path)

file_names = sorted(glob.glob(src_path+'/*.png'))
for file_name in file_names:
    img = cv2.imread(file_name)
    file_name_parse = file_name.split('/')
    print(file_name_parse)
    newfile_name = tar_path+'/'+file_name_parse[-1]
    print(newfile_name)
    rimg=cv2.resize(img,(256,256))
    cv2.imwrite(newfile_name,rimg)
