import cv2

img = cv2.imread(r"C:\Users\suley\Desktop\software\materials\opencv_materials\triangle.png")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
_, thresh = cv2.threshold(gray, 170, 255, cv2.THRESH_BINARY)
contours, _ = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
# gri format yapildi, esik degeri ile siyah beyaz yapildi, konturler bulundu

area = cv2.contourArea(contours[0])
print(area)  # contour degeri ile alan bulundu

perimeter = cv2.arcLength(contours[0], True)
print(perimeter)  # contour degeri ile cevre bulundu

moments = cv2.moments(contours[0])
print(moments["m00"])  # moments degeri ile de alan bulundu
