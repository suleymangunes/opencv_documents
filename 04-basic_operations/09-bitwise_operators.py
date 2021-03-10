import cv2

img1 = cv2.imread(r"C:\Users\suley\Desktop\software\materials\opencv_materials\bitwise_1.png")
img2 = cv2.imread(r"C:\Users\suley\Desktop\software\materials\opencv_materials\bitwise_2.png")

# beyezlar 1'i siyahlar ise 0'i temsil eder.
bit_and = cv2.bitwise_and(img1, img2)  # ve operatoru ile resimler arasi islem yapildi

bit_or = cv2.bitwise_or(img1, img2)  # veya operatoru ile resimler arasi islem yapildi

bit_xor = cv2.bitwise_xor(img1, img2)  # ya da operatoru ile resimler arasi islem yapildi

bit_not = cv2.bitwise_not(img1)  # degil operatoru ile resmin tersi alindi

cv2.imshow("img1", img1)
cv2.imshow("img2", img2)
cv2.imshow("and", bit_and)
cv2.imshow("or", bit_or)
cv2.imshow("xor", bit_xor)
cv2.imshow("not1", bit_not)

cv2.waitKey(0)
cv2.destroyAllWindows()
