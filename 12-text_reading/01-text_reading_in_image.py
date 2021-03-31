from PIL import Image  # grafik isleyen kutuphane ice aktarildi
import pytesseract  # resimde karakterleri algilayan modul ice aktarildi
import cv2  # opencv kutuphanesi ice aktarildi

img1 = cv2.imread(r"C:\Users\suley\Desktop\software\materials\opencv_materials\toplama3.png")
# opencvde islenmesi icin resim ice aktarildi
img = Image.open(r"C:\Users\suley\Desktop\software\materials\opencv_materials\toplama3.png")
# tesseracta kullanmak icin resim farkli degisken ile ice aktarildi

text = pytesseract.image_to_boxes(img, lang="eng")  # resimdeki karakterler string olarak kutu seklinde ekrana yazildi

text = text.split("\n")  # her satir birbirinden ayrildi, her satirini ilk degeri sayi, sonraki degerler koordinat, renk

try:  # eger sonra fazladan bos index var ise kaldirilmasi saglandi
    bos_index = text.index("")  # yok ise devam edildi
    text.pop(bos_index)
except Exception:
    pass

liste = []  # her satirin ilk degerini depolamasi icin liste tanimlandi
row, col, hc = img1.shape  # karakterlerin etrafini saracak dortgenin koordinati icin resmin pencere boyutu alindi

for i in text:  # her satirda sirayla donen ve degeleri bosluk ile ayirip listeye ekleyen dongu tanimlandi
    i = i.split(" ")
    liste.append(i[0])  # her deger listeye string sekilde eklendi
    (x, y, w, h) = int(i[1]), int(i[2]), int(i[3]), int(i[4])  # gelen ilk satirin degerleri sirayla degiskenlere atandi
    cv2.rectangle(img1, (x, row - h), (w , row - y), (0, 255, 0), 2)  # her karakteri saracak dortgen cizildi

print(liste)

cv2.imshow("img", img1)
cv2.waitKey(0)
cv2.destroyAllWindows()
