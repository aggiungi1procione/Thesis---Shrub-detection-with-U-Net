# Thesis: Shrub-detection-with-U-Net







The description of files:
1. tif_to_png.py  -   Python code for bulk conversion of image files in TIF format to PNG format. The second part of the code is the 'slicing' (tiling) algorithm that I used for slicing of the big PNG images into smaller (800 x 800) px tiles. 
2. masks_download_from_JSON.py - Python code for reading the JSON file with URLs of binary masks exported from LabelBox. The code downloads the binary masks and sorts them into separate class masks folders. The second part of the code serves for slicing (100 x 100) px, (200 x 200) px, (300 x 300) px, (400 x 400) px and (500 x 500) px patches from the (800 x 800) px tiles.    
