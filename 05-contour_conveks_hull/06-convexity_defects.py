import cv2

img = cv2.imread(r"C:\Users\suley\Desktop\software\materials\opencv_materials\star.png")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
_, thresh = cv2.threshold(gray, 120, 255, cv2.THRESH_BINARY)
contours, _ = cv2.findContours(thresh, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
# goruntu alindi gri yapildi siyah beyaza cevrildi kontorler bulundu
cnt = contours[0]

hull = cv2.convexHull(cnt, returnPoints=False)  # hull degerlerinin indisleri degiskene atandi
defects = cv2.convexityDefects(cnt, hull)  # kontorler ile hull arasinda kusurlar bulundu

for i in range(defects.shape[0]):  # kusurlarin cizilmesine yetecek kadar donen dongu tanimlandi
    s, e, f, d = defects[i, 0]  # start end far distance degerleri tanimlandi
    start = tuple(contours[0][s][0])  # degerler tuple listesinde saklandi
    end = tuple(contours[0][e][0])
    far = tuple(contours[0][f][0])
    cv2.line(img, start, end, [0, 255, 0], 2)  # degerler ile dis bukey cizildi
    cv2.circle(img, far, 5, [0, 0, 255], -1)  # ve kusur noktalari belirlendi

cv2.imshow("image", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
