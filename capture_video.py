import cv2

capture = cv2.VideoCapture(0)

while True:
    isSuccess, frame = capture.read()
    if not isSuccess:
        break
    cv2.imshow("Video", frame)
    if cv2.waitKey(1) == ord('q'):
        break
capture.release()
cv2.destroyAllWindows()