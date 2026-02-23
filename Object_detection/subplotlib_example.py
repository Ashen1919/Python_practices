import matplotlib.pyplot as plt
import cv2

# read the image
img = cv2.imread("D:/Coding Skill Build/Python Works/python_logo.png", -1)
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

plt.subplot(2, 2, 1)
plt.imshow(img_rgb)
plt.title("Original Image")

plt.subplot(2, 2, 2)
plt.imshow(img_gray)
plt.title("Grayscale Image")

plt.show()
