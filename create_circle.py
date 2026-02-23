import cv2
import numpy as np

image = np.zeros((512, 512, 3), np.uint8)

cv2.circle(image, (256, 256), 100, (0, 0, 255), cv2.FILLED)

cv2.imshow("Circle", image)

cv2.waitKey()
cv2.destroyAllWindows()