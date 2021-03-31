import cv2


def nothing(x):
    pass


img = cv2.imread(r"C:\Users\suley\Desktop\software\materials\opencv_materials\mustang.jpg")
img = cv2.resize(img, (640, 360))
img2 = cv2.imread(r"C:\Users\suley\Desktop\software\materials\opencv_materials\starwars.jpg")
img2 = cv2.resize(img2, (640, 360))

cv2.namedWindow("trackbar")  # resim ve trackbarin eklencegi pencere olusturuldu

cv2.createTrackbar("alpha beta", "trackbar", 0, 1000, nothing)  # tracbar olusturuldu

while True:
    alpha = cv2.getTrackbarPos("alpha beta", "trackbar") / 1000  # trackbarin anlik degeri degiskene atandi
    beta = 1 - alpha  # beta degeri trackbardaki geri kalan degeri aldi

    output = cv2.addWeighted(img, alpha, img2, beta, 0)  # agirlikli toplama islemi yapildi
    cv2.imshow("trackbar", output)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cv2.destroyAllWindows()
