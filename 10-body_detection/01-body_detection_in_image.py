import cv2

img = cv2.imread(r"C:\Users\suley\Desktop\software\materials\opencv_materials\body.jpg")
img = cv2.resize(img, (640, 360))
cascade = cv2.CascadeClassifier(r"C:\Users\suley\Desktop\software\materials\opencv_materials\fullbody.xml")
gray = cv2.cvtColor(img, cv2.COLOR_BGRA2GRAY)
# resim ve cascade dosyalari ice aktarildi resim gri formata donusturuldu ve fonksiyon cascade yardimi ile
# istenilen bolgeleri dikdortgen icine alacak koordinatlar bulundu ve degiskene atandi (bodies)
# bulunan koordinat ile dortgen cizildi

bodies = cascade.detectMultiScale(gray, 1.1, 2)

for (x, y, w, h) in bodies:
    cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 2)

cv2.imshow("img", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
