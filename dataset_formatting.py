import os 
import pandas 
import shutil 
import numpy as np 
import pybboxes as pbx 
from PIL import Image
import csv 

# 乳汁吸附 0
# 機械傷害 1
# 炭疽病 2
# 著色不佳 3
# 黑斑病 4

def turn_row_into_txt(row, image_dict): 

    image = row[0] 
    IMAGE_SIZE = image_dict[image]
    bounding_boxes = [] 
    n = 1
    try:
        while np.isnan(row[n]) == False: 
            # print (row[n])
            img_class = row[n+4]
            if img_class == '不良-乳汁吸附': 
                class_num = 0 
            elif img_class == '不良-機械傷害': 
                class_num = 1
            elif img_class == '不良-炭疽病': 
                class_num = 2 
            elif img_class == '不良-著色不佳': 
                class_num = 3 
            elif img_class == '不良-黑斑病': 
                class_num = 4 
            
            width = row[n+2]/IMAGE_SIZE[0]
            height = row[n+3]/IMAGE_SIZE[1]
            x = (row[n]+width/2)/IMAGE_SIZE[0]
            y = (row[n+1]+height/2)/IMAGE_SIZE[1]
            
            
            
            defect_row = f'{class_num} {x} {y} {width} {height}'
            bounding_boxes.append(defect_row)
            n += 5
        return image, bounding_boxes
    except IndexError: 
        return image, bounding_boxes
    except KeyError: 
        return image, bounding_boxes

import glob
def collect_sizes():
    image_dict = {}
    image_files = glob.glob('C2-Test/C2-Test/*.jpg')
    for file in image_files:
        image_file = file.split('/')[-1]
        image_size = Image.open(file).size
        image_dict[image_file] = image_size
    return image_dict

def return_row(img_dict): 
    filename = 'C2-Test/C2-test.csv'
    file_destination = 'test/labels/'
    df = pandas.read_csv(filename, header=None)
    for index, row in df.iterrows(): 
        txt_name, data = turn_row_into_txt(row, img_dict)
        with open (f'{file_destination}{txt_name}.txt', 'w') as f: 
            for bounding_box in data: 
                f.write(f'{bounding_box}\n')
            
            
        



img_dict = collect_sizes()
return_row(img_dict)
    


    # CSV_PATHS = ['C2-Test/C2-test.csv','C2-Dev/C2-dev.csv', 'C2-Train/C2-train.csv']
    # end_location = ['C2-Test/labels/', 'C2-Dev/labels/', 'C2-Train/labels/']

    # for path_index, value in enumerate(CSV_PATHS): 
    #     df = pandas.read_csv(value, header=None)

    #     for index, row in df.iterrows(): 
    #         name, x_row = turn_row_into_txt(row)
            
    #         with open(f'{end_location[path_index]}.jpg.txt', 'w') as f:
    #             for line in x_row:
    #                 f.write(f"{line}\n")






