# -*- coding: utf-8 -*-
"""
Created on Tue Jun 16 09:52:54 2020

@author: Bibs
"""

from PIL import Image
import glob
import math

#-tif to png converter-

for file in glob.glob('E:/Bianka_Thesis/images_tif/*.tif'):
    img = Image.open(file)                                                      
    img.save(file.replace('tif', 'png'))

#-images to tiles slicer-
tile_dim = 800
img_no=0
for file in glob.glob('E:/Bianka_Thesis/images_png/*.png'):
    img = Image.open(file)   
    img_no+=1
    H_slider = int(tile_dim-((tile_dim-(img.height%tile_dim))/(img.height//tile_dim)))
    W_slider = int(tile_dim-((tile_dim-(img.width%tile_dim))/(img.width//tile_dim)))       #int -> rounding down (can cut off some pixels, but at least won't "create" more)
    
    x=0
    y=0
    tile_no=1
    for i in range(int((img.height-tile_dim)/H_slider)+1):
        for j in range(int((img.width-tile_dim)/W_slider)+1):
            img_crop=img.crop((x,y,x+tile_dim,y+tile_dim))
            img_crop.save('E:/Bianka_Thesis/dataset_tiles/img'+ str(img_no) +'tile'+ str(tile_no) +'.png')
            x+=W_slider 
            j+=1
            tile_no+=1
        y+=H_slider
        x=0
        i+=1
