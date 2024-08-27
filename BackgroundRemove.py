from rembg import remove
from PIL import Image
import pathlib
import os
from tqdm import *

input_path = input('copy your original image path here')
output_path = input('copy your output path here')
lst = os.listdir(input_path)

#only keep image files
image_lst = []
for image in lst:
    if len(image) > 4 and (image[-3:] == 'png' or image[-4:] == 'jpeg' or image[-3:] == 'jpg'):
        image_lst.append(image)

if input_path[-1] == '/':
    input_path = input_path[:-1]
if output_path[-1] == '/':
    output_path = output_path[:-1]

for image in tqdm(image_lst):
    background_remove_image = Image.open(f'{input_path}/{image}')
    background_remove_image = remove(background_remove_image)
    background_remove_image.save(f'{output_path}/background_remove_{image}')

