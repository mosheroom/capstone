#!/usr/bin/python3

import argparse
from PIL import Image

parser = argparse.ArgumentParser(description='Image forgery detection scripts.')
parser.add_argument('--quality', default=95,
                    help='Generates error level analysis for a given photo.')
parser.add_argument('--imagepath', required=True,
                    help='Path to image')

args = parser.parse_args()

def ela(img: str, quality: int):
    '''
    PARAMS:
        img: path to chosen image
        quality: compression rate for JPEG
    '''
    temp_img = f'{img}_ela_{str(quality)}.jpeg'
    try:
        with Image.open(img) as img:
            img.save(temp_img, 'JPEG', quality=quality)
        with Image.open(temp_img) as img2:
            img2.show()
        return 'Success'
    except:
        return f'An error occurred'

def main():
    args = parser.parse_args()
    path = args.imagepath
    quality = args.quality
    ela(img = path, quality = quality)
    print(f'Image located at {path}')

if __name__ == '__main__':
    main()
else:
    print(f'An error has occurred')