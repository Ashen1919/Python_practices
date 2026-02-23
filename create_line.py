import cv2
import numpy as np

# define an image
img_without_floating_point = np.zeros((512, 512, 3), np.uint8)

# create a line
cv2.line(img_without_floating_point, (0, 512), (512, 0), (255, 0, 0), 2)

# show image
cv2.imshow("Image", img_without_floating_point)

cv2.waitKey()
cv2.destroyAllWindows()