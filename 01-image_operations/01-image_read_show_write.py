import cv2  # opencv modulu ice aktarildi

img = cv2.imread(r"C:\Users\suley\Desktop\software\materials\opencv_materials\resim.jpg")
# Resim okundu ve img degiskenine tanimlandi.

img2 = cv2.imread(r"C:\Users\suley\Desktop\software\materials\opencv_materials\resim.jpg", cv2.IMREAD_GRAYSCALE)
# Par1 okunacak resmin adresini ve dosya ismini alır, par2 resme renk efekti verdi. Resim gri tonlarda okundu.(altrnf 0)

cv2.namedWindow("img", cv2.WINDOW_NORMAL)
# Pencere olusturuldu, pencereye resmin tutuldugu degisken atandi, par2 pencerenin yeniden boyutlandirilmasini sagladi

cv2.imwrite(r"C:\Users\suley\Desktop\software\materials\opencv_materials\write_img.jpg", img)
# Olusturulan resim kaydedildi. par1 konum ve resmin ismi, par2 resmin tutuldugu degisken.

cv2.imshow("img", img)  # Resim gosterildi. Par1 pencere ismini, par2 pencereye eklenecek degiskeni alir.
cv2.imshow("img 2", img2)
cv2.waitKey(5000)  # Waitkey ile pencerlerin bekletilmesi saglandi. 1000 = 1 saniye.
cv2.destroyAllWindows()  # Islem sonunda tum pencerelerin kapatilmasi saglandi.
