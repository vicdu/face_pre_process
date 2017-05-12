# import the necessary packages
from skimage.segmentation import slic
from skimage.segmentation import mark_boundaries
from skimage.util import img_as_float
from skimage import io
import matplotlib.pyplot as plt
import argparse
import cv2
'''
# construct the argument parser and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required = True, help = "Path to the image")
args = vars(ap.parse_args())
'''
# load the image and convert it to a floating point data type
image = img_as_float(io.imread("./test1.jpg"))

segments = slic(image, n_segments = 1500, sigma = 5)
means=slic_means(segments)
img_slic=mark_boundaries(image, segments)

'''
cv2.namedWindow("im",2)
cv2.imshow("im",bgr)
cv2.waitKey(0)
'''

fig = plt.figure("Superpixels -- %d segments" % (1500))
ax = fig.add_subplot(1, 1, 1)
ax.imshow(img_slic)
plt.axis("off")
# show the plots
plt.show()

