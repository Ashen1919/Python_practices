import cv2

# read the image
img = cv2.imread("D:/Coding Skill Build/Python Works/python_logo.png", -1)

# convert color scheme
img1 = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
img2 = cv2.cvtColor(img, cv2.COLOR_RGB2HSV)
img3 = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# show image
cv2.imshow('Original', img)
cv2.imshow('Image_RGB', img1)
cv2.imshow('Image_HSV', img2)
cv2.imshow('Image_GRAY', img3)

# avoid closing image immediately
cv2.waitKey()

# to show image until close it.
cv2.destroyAllWindows()