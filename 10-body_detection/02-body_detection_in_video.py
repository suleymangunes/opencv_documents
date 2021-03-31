import cv2

cap = cv2.VideoCapture(r"C:\Users\suley\Desktop\software\materials\opencv_materials\bodies.mp4")
cascade = cv2.CascadeClassifier(r"C:\Users\suley\Desktop\software\materials\opencv_materials\fullbody.xml")
# resimde vucut bulma islemi ile ayni sekilde bulundu.

while True:
    ret, frame = cap.read()
    if ret == 0:
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGRA2GRAY)

    bodies = cascade.detectMultiScale(gray, 1.1, 5)

    for (x, y, w, h) in bodies:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 2)

    cv2.imshow("frame", frame)

    if cv2.waitKey(5) & 0xFF == ord("q"):
        break


cap.release()
cv2.destroyAllWindows()
