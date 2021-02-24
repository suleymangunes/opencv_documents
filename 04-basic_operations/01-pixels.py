import cv2

img = cv2.imread(r"C:\Users\suley\Desktop\software\materials\opencv_materials\resim.jpg")
dimension = img.shape  # resmin yukseklik genislik ve kanal verisini tuple icinde degiskene atadi
print(dimension)

color = img[300, 500]  # resmin belirli noktasindaki pikselin renk degerini aldi
print(color)

blue = img[400, 400, 0]  # remin belirli noktasindaki pikselin mavi renk degerini aldi
print("blue", blue)
green = img[400, 400, 1]
print("green", green)
red = img[400, 400, 2]
print("red", red)

img[420, 500, 0] = 250  # resmin belirli noktasindaki mavi renk degerini degistirdi
print("new blue", img[420, 500, 0])

blue1 = img.item(150, 200, 0)  # resmin belirli noktasindaki mavi renk degerini degiskene atadi
print("blue1 ", blue1)

img.itemset((150, 200, 0), 172)  # atanan degiskenin belirli noktasindaki degeri degistirdi
print("new blue1", img[150, 200, 0])

cv2.imshow("image", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
