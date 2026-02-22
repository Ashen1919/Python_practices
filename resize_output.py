import cv2

# read image
img = cv2.imread("D:/Coding Skill Build/Python Works/python_logo.png", 1)

# define width & length
width, length = 700, 700

# resize the image
resized_img = cv2.resize(img, (width, length))

# show images
cv2.imshow("Image", img)
cv2.imshow("Resized_image", resized_img)

# print scales
print(img.shape)
print(resized_img.shape)

cv2.waitKey(0)
cv2.destroyAllWindows()
