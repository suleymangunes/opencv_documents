import cv2
import numpy as np

img = cv2.imread(r"C:\Users\suley\Desktop\software\materials\opencv_materials\line.png")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
edges = cv2.Canny(gray, 75, 100)
# goruntu okundu, gri formata donusturuldu, kenarlar bulundu

lines = cv2.HoughLinesP(edges, 1, np.pi/180, 10, maxLineGap=120)
# hough donusumu ile kenarlar bulundu

for line in lines:  # bulunan kenarlar kadar donen dongu tanimlandi
    x1, y1, x2, y2 = line[0]  # baslangi ve bitis noktalarinin koordianatlari tanimlandi
    cv2.line(img, (x1, y1), (x2, y2), (0, 255, 0), 2)  # cizgiler cizildi

cv2.imshow("image", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
