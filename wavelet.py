#! /usr/bin/python3

import argparse
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
import pywt

parser = argparse.ArgumentParser(description='Image forgery detection scripts.')
parser.add_argument('--imagepath', required=True,
                    help='Path to image')
args = parser.parse_args()

original = Image.open(args.imagepath)

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