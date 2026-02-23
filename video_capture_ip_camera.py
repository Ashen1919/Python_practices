import cv2

capture = cv2.VideoCapture("http://192.168.8.100:8080/video")

while True:
    isSuccess, frame = capture.read()
    if not isSuccess:
        break
    cv2.imshow("Ip Web cam", frame)
    if cv2.waitKey(1) == ord('q'):
        break
capture.release()
cv2.destroyAllWindows()
