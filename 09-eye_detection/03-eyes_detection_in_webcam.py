import cv2

cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
cascade_face = cv2.CascadeClassifier(r"C:\Users\suley\Desktop\software\materials\opencv_materials\frontalface.xml")
cascade_eye = cv2.CascadeClassifier(r"C:\Users\suley\Desktop\software\materials\opencv_materials\eye.xml")
# video ile tamamiyla ayni sekilde yapildi, sadece goruntu webcamdan alindi

while True:
    ret, frame = cap.read()
    if ret == 0:
        break
    gray = cv2.cvtColor(frame, cv2.COLOR_BGRA2GRAY)

    faces = cascade_face.detectMultiScale(gray, 1.3, 5)

    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x + w, y +h), (0, 255, 0), 2)


    roi_face = frame[y : y + h, x : x + w]
    roi_gray = gray[y : y + h, x : x + w]

    eyes = cascade_eye.detectMultiScale(roi_gray)

    for (ex, ey, ew, eh) in eyes:
        cv2.rectangle(roi_face, (ex, ey), (ex + ew, ey +eh), (0, 0, 255), 2)

    cv2.imshow("frame", frame)
    if cv2.waitKey(2) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()
