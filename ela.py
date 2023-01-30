#!/usr/bin/python3

import argparse
import os
from PIL import Image, ImageChops, ImageEnhance

#TODO
# better error handling - more descriptive error messages at specific places in the code
# add color to output
# check if file already exists
# progress bar

parser = argparse.ArgumentParser(description='Image forgery detection scripts.')
parser.add_argument('--quality', default=95,
                    help='Generates error level analysis for a given photo.')
parser.add_argument('--imagepath', required=True,
                    help='Path to image')
parser.add_argument('--outputname', required=True,
                    help='Desired name for output image')
parser.add_argument('--checkimg',
                    help='Check if given image is a JPEG image format')

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


def ela(img: str, quality: int, output: str) -> str:
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
    # saving img as a temporary image at given quality for analysis
    img.save(temp_img, 'JPEG', quality=quality)
    img2 = Image.open(temp_img)
    # generating an image by calculating the difference between given_img and temp_img
    ela_img = ImageChops.difference(img, img2)
    # getting the min/max of the differences calculated above
    extrema = ela_img.getextrema()
    # getting the largest difference
    max_extrema = max(i[1] for i in extrema)
    # getting the scale for enhancement for each pixel
    divisor = 255.0/max_extrema
    # applying enhancements
    final = ImageEnhance.Brightness(ela_img).enhance(divisor)
    final.save(final_img, 'JPEG')
    final.show()
    os.remove(temp_img)

def main():
    args = parser.parse_args()
    path = args.imagepath
    quality = args.quality
    output_name = args.outputname
    ela(img = path, quality = quality, output = output_name)
    #print(f'Image located at {path}')

if __name__ == '__main__':
    main()
else:
    print(f'An error has occurred')