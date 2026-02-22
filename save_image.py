import cv2

# read image
img = cv2.imread("D:/Coding Skill Build/Python Works/python_logo.png", -1)

# save image on storage
status = cv2.imwrite("D:/Coding Skill Build/Python Works/python_logo_new.png", img)

# check status
print("Image stores success? :", status)