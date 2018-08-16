import sys
import pandas as pd
import shutil
def main():
    list_file_name = sys.argv[1]
    target_path    = sys.argv[2]
    image_paths = pd.read_csv(list_file_name)
    data_length = len(image_paths)
    print(data_length)

    for image_index in range(data_length):
        img_name = image_paths.ix[image_index,0]
        shutil.copy(img_name,target_path)

if __name__== '__main__':
        main()
