import cv2
import numpy as np

# define an image
image = np.zeros((768, 768, 3), np.uint8)

# draw a circle
cv2.circle(image, (384, 384), 370, (255, 255, 255), 3)

# draw the eyes
cv2.circle(image, (220, 220), 78, (255, 255, 255), 3)
cv2.circle(image, (220, 220), 40, (255, 0, 0), cv2.FILLED)

cv2.circle(image, (550, 220), 78, (255, 255, 255), 3)
cv2.circle(image, (550, 220), 40, (255, 0, 0), cv2.FILLED)

# draw mouth
cv2.line(image, (200, 560), (600, 560), (0, 0, 255), 3)

cv2.imshow("Face Image", image)
cv2.waitKey()
cv2.destroyAllWindows()