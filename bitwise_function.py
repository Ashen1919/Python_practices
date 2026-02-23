import cv2
import numpy as np

# read the image
img1 = cv2.imread("D:/Coding Skill Build/Python Works/python_logo.png", -1)
img2 = np.zeros_like(img1)
img2[100:300, 100:300] = 255

# apply bitwise function
# final_image = cv2.bitwise_not(img)
# img_and = cv2.bitwise_and(img1, img2)
# img_and = cv2.bitwise_or(img1, img2)
img_and = cv2.bitwise_xor(img1, img2)

# save the image
# cv2.imwrite("D:/Coding Skill Build/Python Works/python_logo_bit_not.png", final_image)
# cv2.imwrite("D:/Coding Skill Build/Python Works/python_logo_bit_and.png", img_and)
# cv2.imwrite("D:/Coding Skill Build/Python Works/python_logo_bit_or.png", img_and)
cv2.imwrite("D:/Coding Skill Build/Python Works/python_logo_bit_xor.png", img_and)