import cv2

cap = cv2.VideoCapture(r"C:\Users\suley\Desktop\software\materials\opencv_materials\faces.mp4")
cascade = cv2.CascadeClassifier(r"C:\Users\suley\Desktop\software\materials\opencv_materials\frontalface.xml")
# video ve cascade dosyasi ice aktarildi

while True:
    ret, frame = cap.read()
    if ret == 0:
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGRA2GRAY)
    faces = cascade.detectMultiScale(gray, 1.1, 7)  # foto griye cevrildi ve cascade dosyasi ile degerler bulundu

    for (x, y, w, h) in faces:  # bulunan degereler koordinat iceriyordu
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 2)  # belirlenen bolgelere dortgen cizildi

    cv2.imshow("img", frame)

    if cv2.waitKey(3) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()
