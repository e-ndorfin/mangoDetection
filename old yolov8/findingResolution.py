from PIL import Image 
import os 
import shutil 
from rembg import remove 

def remove_background(): 
    dir = 'testing'

    for img in os.listdir(dir):
        input_path = f'{dir}/{img}'
        export_path = f'output{img[:-4]}.png'

        inp = Image.open(input_path)
        # inp = inp.convert('RGB')
        output = remove(inp)
        output.save(export_path)


# {'1280x720': 19339, '1344x1008': 3801, '1536x1152': 490, '1152x1536': 1649, '1088x816': 462, '816x816': 27}

def sorting_invalid_resolutions(): 

    directory = 'train/images'

    resolution_dict = {} 

    for image in os.listdir(directory): 
        image_loc = f'train/images/{image}'
        img = Image.open(image_loc)
        width, height = img.size

        try: 
            if (width, height) == (1280,720): 
                shutil.move(image_loc, 'train/others')
        except PermissionError: 
            continue

        # try: 
        #     resolution_dict[f'{width}x{height}'] += 1 
        # except KeyError: 
        #     resolution_dict[f'{width}x{height}'] = 1 

    # print (resolution_dict) 

def altering_resolution(): 
    directory = 'train/images' 

    for img in os.listdir(directory):
        img_path = f'{directory}/{img}'

        pil_image = Image.open(img_path)
        pil_image = pil_image.resize((640,640))
        pil_image.save(img_path)
    
    directory = 'valid/images' 

    for img in os.listdir(directory):
        img_path = f'{directory}/{img}'

        pil_image = Image.open(img_path)
        pil_image = pil_image.resize((640,640))
        pil_image.save(img_path)

remove_background()
