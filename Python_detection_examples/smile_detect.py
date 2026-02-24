import cv2

# Load haar cascades
face_cascade = cv2.CascadeClassifier("D:/Coding Skill Build/Python Works/haarcascade_frontalface_default.xml")
smile_cascade = cv2.CascadeClassifier("D:/Coding Skill Build/Python Works/haarcascade_smile.xml")

# capture video
capture = cv2.VideoCapture(0)

while True:
    isSuccess, frame = capture.read()
    if isSuccess:
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # detect faces
        faces = face_cascade.detectMultiScale(gray, 1.3, 5)

        for (x, y, w, h) in faces:
            # Draw face rectangle
            cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)

            # Region of interest for smile detection
            face_roi_gray = gray[y:y + h, x:x + w]
            face_roi_color = frame[y:y + h, x:x + w]

            # Detect smile
            smiles = smile_cascade.detectMultiScale(
                face_roi_gray,
                scaleFactor=1.7,
                minNeighbors=22
            )

            # Draw smile rectangle
            for (sx, sy, sw, sh) in smiles:
                cv2.rectangle(face_roi_color, (sx, sy), (sx + sw, sy + sh), (0, 255, 0), 2)
                cv2.putText(frame, "Smile Detected :)", (x, y - 10),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)
                break

        cv2.imshow("Smile Detector", frame)
    else:
        print("Camera doesn't open")
        # Press 'q' to quit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

capture.release()
cv2.destroyAllWindows()