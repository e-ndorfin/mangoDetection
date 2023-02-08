import os 
import pandas 
import shutil 
import numpy as np 
import pybboxes as pbx 

# 乳汁吸附 0
# 機械傷害 1
# 炭疽病 2
# 著色不佳 3
# 黑斑病 4

def turn_row_into_txt(row, IMAGE_SIZE=(640,640)): 

    image = row[0] 
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

            width = row[n+2]/IMAGE_SIZE[0]/2
            height = row[n+3]/IMAGE_SIZE[0]/1.125
            x = (row[n]+width/2)/IMAGE_SIZE[0]/2
            y = (row[n+1]+height/2)/IMAGE_SIZE[1]/1.125
            
            
            defect_row = f'{class_num} {x} {y} {width} {height}'
            bounding_boxes.append(defect_row)
            n += 5
        return image, bounding_boxes
    except IndexError: 
        return image, bounding_boxes
    except KeyError: 
        return image, bounding_boxes


# print(turn_row_into_txt(['14786.jpg',455,304,233,271,'不良-黑斑病',837.0,461.0,16.0,18.0,'不良-炭疽病',600.0,618.0,34.0,29.0,'不良-炭疽病']))   

# CSV_PATH = 'C2-Train\C2-Train.csv'
# end_location = 'train/labels/'

def main(): 

    CSV_PATH = 'C2-Test\C2-test.csv'
    end_location = 'valid/labels/'

    df = pandas.read_csv(CSV_PATH, header=None)

    for index, row in df.iterrows(): 
        name, x_row = turn_row_into_txt(row)
        

        with open(f'{end_location}{name[:-4]}.txt', 'w') as f:
            for line in x_row:
                f.write(f"{line}\n")

main()

