import cv2

# capture video
capture = cv2.VideoCapture(0)

# Load pre-trained model
face_cascade = cv2.CascadeClassifier("D:/Coding Skill Build/Python Works/haarcascade_frontalface_default.xml")

# detect faces
while True:
    isSuccess, frame = capture.read()
    if isSuccess:
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, 1.1, 5)

        for (x, y, w, h) in faces:
            cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 0, 255), 2)
            cv2.putText(frame, "Face Detected", (x, y+h+20), cv2.FONT_ITALIC, 1.7, (0, 0, 0), 4)
        cv2.imshow("Face detection", frame)
    else:
        print("Camera doesn't open.")
    if cv2.waitKey(1) == ord('q'):
        break
capture.release()
cv2.destroyAllWindows()


