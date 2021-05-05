"""

Concept based on: https://bi1.caltech.edu/code/t07_clicking_image_analysis.html

"""
import sys
import json
import numpy as np # our numerical workhorse
import matplotlib.pyplot as plt # plotting library
import seaborn as sns # extra plotting features
import skimage.io # image analysis functionality

# read the image using scikit-image
impath = sys.argv[1]
im = skimage.io.imread(impath)

# This removes the default white grid placed by seaborn but only for this plot
with sns.axes_style("white"):
    plt.imshow(im)

# Do annotations
annotations = []
do_annotation = True
while do_annotation:
    clicks = plt.ginput(1) # Will record one click
    note = input('Enter note: ')
    another = input('Add another? (y/n) ')
    do_annotation = True if another == 'y' else False
    annotations.append({
        'clicks': clicks,
        'note': note
    })
    print('-'*40)

# Write annotations to metadata file
with open('{}.meta.json'.format(impath), 'w') as f:
    f.write(json.dumps(annotations, indent=4))
