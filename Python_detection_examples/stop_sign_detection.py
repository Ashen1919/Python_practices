import cv2

capture = cv2.VideoCapture(0)

sign_cascade = cv2.CascadeClassifier("D:/Coding Skill Build/Python Works/Stopsign_HAAR_19Stages.xml")

while True:
    isSuccess, frame = capture.read()
    if isSuccess:
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        signs = sign_cascade.detectMultiScale(gray, 1.1, 5)

        for (x, y, w, h) in signs:
            cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 0, 255), 2)
            cv2.putText(frame, "Stop", (x, y+h+20), cv2.FONT_ITALIC, 1.7, (0, 255, 0), 2)
        cv2.imshow("Road sign", frame)
    else:
        print("Camera doesn't open.")
    if cv2.waitKey(1) == ord('q'):
        break

capture.release()
cv2.destroyAllWindows()