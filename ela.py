#!/usr/bin/python3

import argparse
from PIL import Image

#TODO
# better error handling - more descriptive error messages 
# at specific places in the code
# add more useful ELA output - make the differences more apparent 
# add a function to check if the given image is a JPEG
# add color to output

parser = argparse.ArgumentParser(description='Image forgery detection scripts.')
parser.add_argument('--quality', default=95,
                    help='Generates error level analysis for a given photo.')
parser.add_argument('--imagepath', required=True,
                    help='Path to image')
parser.add_argument('--checkimg',
                    help='Check if given image is a JPEG image format')

args = parser.parse_args()

def jpeg_verify(img: str) -> bool:
    '''
    PARAMS:
        IMG: path to chosen image
    '''

    with Image.open(img) as img:
        if img.format() == 'JPEG':
            return True
        else:
            return False

def ela(img: str, quality: int) -> str:
    '''
    PARAMS:
        img: path to chosen image
        quality: compression rate for JPEG
    '''
    if jpeg_verify(img) == True:
        pass
    else:
        print('The given image is not a JPEG. Please provide an image in JPEG format')
        quit()
    temp_img = f'{img}_ela_{str(quality)}.jpeg'
    try:
        with Image.open(img) as img:
            img.save(temp_img, 'JPEG', quality=quality)
        with Image.open(temp_img) as img2:
            img2.show()
        return 'Success'
    except:
        return f'There was something wrong with the image given. Check if it\'s a JPEG.'

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