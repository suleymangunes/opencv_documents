import cv2

img = cv2.imread(r"C:\Users\suley\Desktop\software\materials\opencv_materials\resim.jpg")

img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)  # resim bgr formatindan rgb formatina donusturuldu
img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)  # resim hsv formatina donusturuldu
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  # resim gray formatina donusturuldu

cv2.imshow("original", img)
cv2.imshow("rgb", img_rgb)
cv2.imshow("hsv", img_hsv)
cv2.imshow("gray", img_gray)

cv2.waitKey(0)
cv2.destroyAllWindows()
