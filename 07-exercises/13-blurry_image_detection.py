import cv2

img = cv2.imread(r"C:\Users\suley\Desktop\software\materials\opencv_materials\mustang.jpg")

img2 = cv2.medianBlur(img, 3)

laplacian1 = cv2.Laplacian(img2, cv2.CV_64F).var()  # resmin blurluguna gore deger gonderir
laplacian2 = cv2.Laplacian(img, cv2.CV_64F).var()  # blur en az 3 degeri alacagi icin ona gore kosul yazilabilir

if laplacian1 < 400:

    print(laplacian1)
    print("blurlu resimdir")
else:
    print("degildir")

print(laplacian2)

cv2.imshow("img", img)
cv2.imshow("img2", img2)
cv2.waitKey(0)
cv2.destroyAllWindows()
