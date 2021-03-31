import cv2
# icinde n ve  p diye klasorler bulunana ve n klasorunde negatif yani istenilen goruntu disinda herhangi bir seyi iceren
# nesnelerin oldugu goruntuler p klasorunde ise sadece istenilen goruntuleri iceren nesnelerin bulundugu haar cascade
# klasoru olusturulur. programda egitim baslatilir. egitim sonunda dosyada cascade dosyasi olusmus olur.

cap = cv2.VideoCapture(r"C:\Users\suley\Desktop\software\materials\opencv_materials\car.mp4")

cascade_mine = cv2.CascadeClassifier(r"C:\Users\suley\Desktop\software\materials\opencv_materials"
                                     r"\car_cascade\classifier\cascade.xml")
# bizim olusturdugumuz cascade dosyasi
cascade_others = cv2.CascadeClassifier(r"C:\Users\suley\Desktop\software\materials\opencv_materials\car_cascade.xml")
# hazir alinan cascade dosyasi

while True:
    ret, frame = cap.read()
    if ret == 0:
        break
    frame = cv2.resize(frame, (640, 360))
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    cars_mine = cascade_mine.detectMultiScale(gray, 1.1, 1)
    cars_other = cascade_others.detectMultiScale(gray, 1.1, 1)

    for (x, y, w, h) in cars_mine:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 2)

    for (xo, yo, wo, ho) in cars_other:
        cv2.rectangle(frame, (xo, yo), (xo + wo, yo + ho), (0, 255, 0), 2)

    cv2.imshow("frame", frame)

    if cv2.waitKey(5) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()
