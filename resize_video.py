import cv2

# capture a video
capture = cv2.VideoCapture("D:/Coding Skill Build/Python Works/sample_video.mp4")

# define width & height
frameWidth = 256
frameHeight = 256

# resize video
capture.set(3, frameWidth)
capture.set(4, frameHeight)

# run video until it quit
while True:
    isSuccess, frame = capture.read()
    if not isSuccess:
        break
    cv2.imshow("Video", frame)
    if cv2.waitKey(1) == ord('q'):
        break
capture.release()
cv2.destroyAllWindows()