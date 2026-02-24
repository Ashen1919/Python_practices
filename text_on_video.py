import cv2

capture = cv2.VideoCapture("D:/Coding Skill Build/Python Works/sample_video.mp4")

while True:
    isSuccess, frame = capture.read()
    if not isSuccess:
        break
    cv2.putText(frame, "River video", (10, 100), cv2.FONT_HERSHEY_DUPLEX, 1.2, (255, 255, 255), 4)
    cv2.imshow("Video_capture", frame)
    if cv2.waitKey(1) == ord('q'):
        break
capture.release()
cv2.destroyAllWindows()