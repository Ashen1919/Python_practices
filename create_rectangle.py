import cv2
import numpy as np

image = np.zeros((512, 512, 3), np.uint8)

cv2.rectangle(image, (100, 100), (300, 300), (255, 0, 255), 3)

cv2.imshow("Image", image)

cv2.waitKey()
cv2.destroyAllWindows()