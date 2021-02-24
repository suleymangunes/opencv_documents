import cv2

img = cv2.imread(r"C:\Users\suley\Desktop\software\materials\opencv_materials\resim.jpg")
print(img.shape)

roi = img[50: 420, 350: 720]  # yukseklik olarak 50 den 420ye genislik olarak 350den 720ye kadar aldi (kirpma islemi)

cv2.imshow("image", img)
cv2.imshow("roi", roi)
cv2.waitKey(0)
cv2.destroyAllWindows()
