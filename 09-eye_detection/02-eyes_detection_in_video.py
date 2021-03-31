import cv2

cap = cv2.VideoCapture(r"C:\Users\suley\Desktop\software\materials\opencv_materials\eyes.mp4")
cascade_face = cv2.CascadeClassifier(r"C:\Users\suley\Desktop\software\materials\opencv_materials\frontalface.xml")
cascade_eye = cv2.CascadeClassifier(r"C:\Users\suley\Desktop\software\materials\opencv_materials\eye.xml")
# resimde bulma ile ayni islemler yapildi, her frame uzerinde tekrarlandi ve degerler bulundu

while True:
    ret, frame = cap.read()
    if ret == 0:
        break
    gray = cv2.cvtColor(frame, cv2.COLOR_BGRA2GRAY)

    faces = cascade_face.detectMultiScale(gray, 1.5, 9)

    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x + w, y +h), (0, 255, 0), 2)

    roi_face = frame[y : y + h, x : x + w]
    roi_gray = gray[y : y + h, x : x + w]

    eyes = cascade_eye.detectMultiScale(roi_gray, 1.1, 4)

    for (ex, ey, ew, eh) in eyes:
        cv2.rectangle(roi_face, (ex, ey), (ex + ew, ey +eh), (0, 0, 255), 2)

    cv2.imshow("frame", frame)
    if cv2.waitKey(2) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()
