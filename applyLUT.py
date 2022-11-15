import numpy as np
import cv2

b_max = 230
g_max = 220
r_max = 250

identity = np.arange(256, dtype = np.dtype('uint8'))

b_channel = np.arange(b_max, dtype = np.dtype('uint8'))
b_channel = np.append(b_channel, (256-b_max)*[b_max])
g_channel = np.arange(g_max, dtype = np.dtype('uint8'))
g_channel = np.append(g_channel, (256-g_max)*[g_max])
r_channel = np.arange(r_max, dtype = np.dtype('uint8'))
r_channel = np.append(r_channel, (256-r_max)*[r_max])

if 256 != b_channel.size or 256 != g_channel.size or 256 != r_channel.size:
    print "size of arrays don't match!"

lut = np.dstack((identity, identity, b_channel, g_channel, r_channel))

# Load the image
img = cv2.imread('input.jpg',cv2.IMREAD_COLOR)
dstImage = cv2.LUT(img, lut)
cv2.imwrite('output.jpg', dstImage)
