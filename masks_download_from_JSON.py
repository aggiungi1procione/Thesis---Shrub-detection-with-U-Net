Created on Tue Aug 25 10:49:34 2020

@author: Bibs
"""

import json
import urllib.request
import glob
from PIL import Image

#-reads JSON file (exported from LabelBox) with URLs of binary masks-
#-downloads them and sorts them into separate class masks folders-
#the LabelBox EXPORT JSON file is a LIST OF DICTIONARIES: [ {"name": "Tom", "age": 10}, {"name": "Mark", "age": 5}, {"name": "Pam", "age": 7} ]

with open('PATH/LabelBox_export_25.8.json') as f:
  exp_file = json.load(f)
  
for x in exp_file:
    for y in x['Label']['objects']:
        combo = {'ID': x['External ID'],
                        'Mask': y['instanceURI'],
                        'Name': y['title']}
        path = 'PATH/test1/test1_mask_' + combo['Name'] + '/' + combo['ID'].split('.')[0] + '_' + combo['Name'] + '.png'
        urllib.request.urlretrieve(combo['Mask'], path)


#-slicer of image tiles and masks to smaller tiles acceptable by ML model-

model_tile_dim = 100        #dimension of tiles for the used ML model
for folder in glob.glob('PATH/test1/*'):
    for file in glob.glob(folder + '/*.png'):        
        img = Image.open(file)  
        if (img.height%model_tile_dim) == 0:
            slider = int(model_tile_dim) 
            #W_slider = H_slider 
        else:
            slider = int(model_tile_dim-((model_tile_dim-(img.height%model_tile_dim))/(img.height//model_tile_dim)))
            #W_slider = H_slider      
        x=0
        y=0
        tile_no=1
        for i in range(int((img.height-model_tile_dim)/slider)+1):
            for j in range(int((img.width-model_tile_dim)/slider)+1):
                img_crop=img.crop((x, y, x + model_tile_dim, y + model_tile_dim))
                #img_crop.save(folder.split('test1')[0] + 'test1_model_dims_dataset/' + file.split('\\')[1] + '/' + file.split('\\')[2].split('.')[0] + '_' + str(tile_no) +'.png')
                img_crop.save(folder.split('test1')[0] + 'test1_model_dims_dataset/' + file.split('\\')[1] + '/' + file.split('\\')[2].split('.')[0].split('_')[0] + '_' + str(tile_no) +'.png')
                x+=slider 
                j+=1
                tile_no+=1
            y+=slider
            x=0
            i+=1
