import cv2
import numpy as np

# Read color image
img = cv2.imread('download.jpg', 1)

# Get the image's height, width, and channels
height, width, depth = img.shape

# Create blank YCrCb image
img_ycrcb = np.zeros((height, width, 3))

# ======================================================
# IMPLEMENTATION USING OPENCV LIBRARY
# ======================================================
# img_ycrcb = cv2.cvtColor(img, cv2.COLOR_BGR2YCR_CB)

# ======================================================
# IMPLEMENTATION WITHOUT OPENCV LIBRARY
# ======================================================


# kalkulasi
for i in np.arange(height):
    for j in np.arange(width):
        r = img.item(i, j, 0)
        g = img.item(i, j, 1)
        b = img.item(i, j, 2)

        # Default RGB to YCbCr equation
        #        Y = (0.299*r) + (0.587*g) + (0.114*b)
        #        U = b - Y
        #        V = r - Y
        #        Cb = U / (1.772+0.5)
        #        Cr = V / (1.402+0.5)

        # RGB to YCbCr and representing it in 255
        Y = 16 + ((65.481 * r) / 256. + (128.553 * g) / 256. + (24.966 * b) / 256.)
        Cb = 128 + ((-37.797 * r) / 256. - (74.203 * g) / 256. + (112.0 * b) / 256.)
        Cr = 128 + ((112.0 * r) / 256. - (93.786 * g) / 256. - (18.214 * b) / 256.)

        img_ycrcb.itemset((i, j, 0), Y)
        img_ycrcb.itemset((i, j, 1), Cr)
        img_ycrcb.itemset((i, j, 2), Cb)

# Write image
cv2.imwrite('image_ycrcb.jpg', img_ycrcb)
# View image
cv2.imshow('image', img_ycrcb)
cv2.waitKey(0)
cv2.destroyAllWindows()