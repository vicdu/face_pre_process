# -*- coding: utf-8 -*-
from skimage.segmentation import slic
from skimage.segmentation import mark_boundaries
from skimage.util import img_as_float,regular_grid,regular_seeds
from skimage import io
import matplotlib.pyplot as plt
import argparse
import cv2
import numpy as np
from slic_means import slic_means
'''
# construct the argument parser and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required = True, help = "Path to the image")
args = vars(ap.parse_args())
'''
def slic_output(img):
#    img = cv2.imread('./test1.jpg')
    image = img_as_float(img)
    #slices = regular_grid(image.shape[:3], 1500)
    #seed_img=regular_seeds(image.shape[:3],1500)

    segments = slic(image, n_segments = 1500, sigma = 5)

    #img_slic是指在原图上划线，img是指生成的平均脸
    slic_means_face = slic_means(img,segments)

    img_slic=mark_boundaries(image, segments)

    return slic_means_face
'''

    cv2.namedWindow("im",2)
    cv2.imshow("im",slic_means_face)
    cv2.waitKey(0)

#显示原图上划线
fig = plt.figure("Superpixels -- %d segments" % (1500))
ax = fig.add_subplot(1, 1, 1)
ax.imshow(img_slic)
plt.axis("off")
# show the plots
plt.show()
'''