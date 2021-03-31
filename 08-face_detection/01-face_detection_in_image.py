import cv2

img = cv2.imread(r"C:\Users\suley\Desktop\software\materials\opencv_materials\face.png")
# resim dosyasi ice aktarildi
face_cascade = cv2.CascadeClassifier(r"C:\Users\suley\Desktop\software\materials\opencv_materials\frontalface.xml")
# yuz bulan haar cascade dosyasi ice aktarildi
gray = cv2.cvtColor(img, cv2.COLOR_BGRA2GRAY)  # resim gri formata cevrildi
faces = face_cascade.detectMultiScale(gray, 1.3, 7)  # gray uzerinde yuz olan bolgelerin koordinatlarini degiskene atadi
#par2 olceklendirmeyi gosterir, ne kadar kucuk o kadar fazla deger
# par3 belirli bolgede bulunacak yuz sayisini belirtir, yani belrili bolgede tarama yapilirlen en az 7 kez bulmali

for (x, y, w, h) in faces:  # bulunan yuz degerlerine dongu icinde dortgen cizilmesi saglandi
    cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)

cv2.imshow("img", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
