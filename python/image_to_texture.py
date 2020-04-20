"""
Give path of a directory contain images to this script.
make a direcotry with name Textures. then create texture from images and save in the Textures directory.
"""

import os
import shutil
from PIL import Image

path = input('Please enter path: ')
try:
    os.chdir(path)
except:
    exit()

os.mkdir('Textures')

# Get all files from directory then filter images.
images = [file for file in os.listdir() if file.endswith('jpg') or file.endswith('png')]

# Copy all images to the Textures directory.
for img in images:
    shutil.copy(img, 'Textures')

os.chdir('Textures')

# Create texture from images and save.
for img in images:
    with Image.open(img) as this_image:
        this_image.paste(this_image, (1, 1))
        this_image.save(img)
