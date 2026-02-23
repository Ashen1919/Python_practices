import cv2
import numpy as np

# Image without floating points
img_without_floating_point = np.zeros((512, 512, 3), np.uint8)

img_without_floating_point[20:50, 160:500] = 255, 0, 0
img_without_floating_point[20:500, 50:80] = 0, 255, 0

# fill static color on entire image
# img_without_floating_point[:] = 0, 255, 0

# show image
cv2.imshow("Image", img_without_floating_point)

cv2.waitKey(0)
cv2.destroyAllWindows()