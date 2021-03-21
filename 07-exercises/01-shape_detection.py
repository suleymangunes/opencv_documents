import cv2

font1 = cv2.FONT_HERSHEY_SIMPLEX
img = cv2.imread(r"C:\Users\suley\Desktop\software\materials\opencv_materials\polygons.png")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
ret, thresh = cv2.threshold(gray, 240, 255, cv2.THRESH_BINARY)
contours, ret2 = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
# contour = bir rengin veya yogunluğunun sahip olduğu tum surekli noktaları birlestiren kapalı bir egridir

for cnt in contours:

    epsilon = 0.01 * cv2.arcLength(cnt, True)
    approx = cv2.approxPolyDP(cnt, epsilon, True)  # konturleri alip kenarlari sayan fonskiyon tanimlandi
    # approx bulunan her geomterik sekilde sira ile kose koordinatlarini 2 boyutlu sekilde aldi

    cv2.drawContours(img, [approx], 0, 0, 3)  # konturler cizildi

    x = approx.ravel()[0]  # iki boyutlu approx degerlerini tek boyuta cekildi ve degerleri x y degiskenine atandi
    y = approx.ravel()[1]  # bu sayede yazinin yazialacagi koordinat belirlenmis oldu

    if len(approx) == 3:
        cv2.putText(img, "triangle", (x + 10, y), font1, 0.5, (0, 0, 255))
    elif len(approx) == 4:
        cv2.putText(img, "rectangle", (x + 5, y + 20), font1, 0.5, (0, 0, 255))
    elif len(approx) == 5:
        cv2.putText(img, "pentagon", (x + 10, y), font1, 0.5, (0, 0, 255))
    elif len(approx) == 6:
        cv2.putText(img, "hexagon", (x + 10, y), font1, 0.5, (0, 0, 255))
    else:
        cv2.putText(img, "ellipse", (x + 10, y), font1, 0.5, (0, 0, 255))


cv2.imshow("img", img)
cv2.imshow("gray", gray)
cv2.imshow("thresh", thresh)
cv2.waitKey(0)
cv2.destroyAllWindows()
