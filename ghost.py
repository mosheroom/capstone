#!/usr/bin/python3

import argparse
import os
from PIL import Image, ImageChops, ImageEnhance




# Exposing Digital Forgeries from JPEG ghosts
# https://farid.berkley.edu/downloads/publications/tifs09.pdf


parser = argparse.ArgumentParser(description='Image forgery detection scripts.')
parser.add_argument('-q', '--quality', default=95,
                    help='Generates error level analysis for a given photo.')
parser.add_argument('-p', '--imagepath', required=True,
                    help='Path to image')
parser.add_argument('-on', '--outputname', required=True,
                    help='Desired name for output image')

args = parser.parse_args()

def jpeg_verify(img: str) -> bool:
    '''
    PARAMS:
        IMG: path to chosen image
    '''

    with Image.open(img) as image:
        if image.format == 'JPEG':
            return True
        else:
            return False


def ghost(img: str, quality: int, output: str) -> str:
    '''
    PARAMS:
        img: path to chosen image
        quality: compression rate for JPEG
    '''

    '''
    if jpeg_verify(img) == True:
        pass
    else:
        print('The given image is not a JPEG. Please provide an image in JPEG format')
        quit()
    '''
    given_img = img
    temp_img = f'{img}_temp.jpeg'
    final_img = output
    
    img = Image.open(given_img)
    width, height = img.size
    # saving img as a temporary image at given quality for analysis
    img.save(temp_img, 'JPEG', quality=quality)
    img2 = Image.open(temp_img)
    # generating an image by calculating the difference between given_img and temp_img
    ghost_img = ImageChops.difference(img, img2)
    # squaring the difference
    diff_squared = ghost_img**2

    # jpeg blocks
    block = 16

