import cv2

# capture a video
capture = cv2.VideoCapture("D:/Coding Skill Build/Python Works/sample_video.mp4")

# run video until it quit
while True:
    isSuccess, frame = capture.read()
    if not isSuccess:
        break
    # rotate video
    r1 = cv2.rotate(frame, cv2.ROTATE_90_COUNTERCLOCKWISE)
    r2 = cv2.rotate(frame, cv2.ROTATE_90_CLOCKWISE)
    r3 = cv2.rotate(frame, cv2.ROTATE_180)

    # show video
    cv2.imshow("Rotate 01", r1)
    cv2.imshow("Rotate 02", r2)
    cv2.imshow("Rotate 03", r3)
    cv2.imshow("Original", frame)

    if cv2.waitKey(1) == ord('q'):
        break
capture.release()
cv2.destroyAllWindows()