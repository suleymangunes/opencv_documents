import cv2

cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
cascade = cv2.CascadeClassifier(r"C:\Users\suley\Desktop\software\materials\opencv_materials\frontalface.xml")
# webcamdan goruntu alindi ve cascade dosyasi ice aktarildi

while True:
    ret, frame = cap.read()

    if ret == 0:
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGRA2GRAY)
    faces = cascade.detectMultiScale(gray, 1.3, 7)  # cascade ile degerler bulundu ve degiskene atandi

    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 2)

    cv2.imshow("img", frame)

    if cv2.waitKey(3) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()
