#!/usr/bin/python3

import argparse
import os
from time import sleep
from PIL import Image, ImageChops, ImageEnhance
import pywt
import numpy as np
import matplotlib.pyplot as plt



parser = argparse.ArgumentParser(description='Image forgery detection scripts.')
parser.add_argument('--quality', default=95,
                    help='Generates error level analysis for a given photo.')
parser.add_argument('--imagepath', required=True,
                    help='Path to image')
parser.add_argument('--outputname',
                    help='Desired name for output image')
parser.add_argument('--ela', 
                    help='ELA output. Requires quality argument, image path argument, and output name argument')
parser.add_argument('--wavelet', 
                    help='Wavelet transform')

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

    if jpeg_verify(img) == True:
        pass
    else:
        print('Error: Given image is not in a JPEG format')
        exit()

    given_img = img
    temp_img = f'{img}_temp.jpeg'
    final_img = output
    
    img = Image.open(given_img)
    print(f'Creating temporary image')
    sleep(1)
    # saving img as a temporary image at given quality for analysis
    print(f'Saving temporary image at {quality} quality')
    sleep(1)
    img.save(temp_img, 'JPEG', quality=quality)
    img2 = Image.open(temp_img)
    # generating an image by calculating the difference between given_img and temp_img
    print(f'Calculating difference between original and test image')
    sleep(1)
    ela_img = ImageChops.difference(img, img2)
    # getting the min/max of the differences calculated above
    print(f'Calculating extrema of differences calculated')
    sleep(1)
    extrema = ela_img.getextrema()
    # getting the largest difference
    max_extrema = max(i[1] for i in extrema)
    # getting the scale for enhancement for each pixel
    divisor = 255.0/max_extrema
    # applying enhancements
    print(f'Generating final image')
    sleep(1)
    final = ImageEnhance.Brightness(ela_img).enhance(divisor)
    final.save(final_img, 'JPEG')
    final.show()
    os.remove(temp_img)

def wavelet(imagepath):
    original = Image.open(imagepath)

    # Wavelet transform of image, and plot approximation and details
    titles = ['Approximation', ' Horizontal detail',
            'Vertical detail', 'Diagonal detail']
    coeffs2 = pywt.dwt2(original, 'bior1.3')
    LL, (LH, HL, HH) = coeffs2
    fig = plt.figure(figsize=(12, 3))
    for i, a in enumerate([LL, LH, HL, HH]):
        ax = fig.add_subplot(1, 4, i + 1)
        ax.imshow(a, interpolation="nearest", cmap=plt.cm.gray)
        ax.set_title(titles[i], fontsize=10)
        ax.set_xticks([])
        ax.set_yticks([])

fig.tight_layout()
plt.show()

def main():
    args = parser.parse_args()
    path = args.imagepath
    quality = args.quality
    output_name = args.outputname

    if args.ela != None:
        ela(img = path, quality = quality, output = output_name)
    elif args.wavelet != None:
        wavelet(imagepath = path)
    #print(f'Image located at {path}')

if __name__ == '__main__':
    main()
else:
    print(f'An error has occurred')