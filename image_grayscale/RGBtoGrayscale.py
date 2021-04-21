import numpy as np
import cv2

# Read color image
img = cv2.imread('flower.jpg')

# Get the image's height, width, and channels
height, width, channel = img.shape

# Create blank grayscale image
img_grayscale = np.zeros((height,width,1))

# ======================================================
# IMPLEMENTATION USING OPENCV LIBRARY
# ======================================================
# img_grayscale = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# ======================================================
# IMPLEMENTATION WITHOUT OPENCV LIBRARY
# ======================================================

# CALCULATE
for i in np.arange(height):
    for j in np.arange(width):
        r = img.item(i,j,0)
        g = img.item(i,j,1)
        b = img.item(i,j,2)

        # RGB to Grayscale
        y = 0.299*r + 0.587*g + 0.144*b

        img_grayscale.itemset((i,j,0),int(y))

# Write image
cv2.imwrite('image_grayscale.jpg',img_grayscale)
# View image
cv2.imshow('image',img_grayscale)
cv2.waitKey(0)
cv2.destroyAllWindows()