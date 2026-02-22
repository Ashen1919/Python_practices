import cv2

# read the image
img = cv2.imread("D:/Coding Skill Build/Python Works/python_logo.png", -1)

# show image
cv2.imshow('Image', img)

# avoid closing image immediately
cv2.waitKey()

# to show image until close it.
cv2.destroyAllWindows()