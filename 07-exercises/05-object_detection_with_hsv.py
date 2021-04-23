import cv2
import numpy as np

def nothing(x):
    pass


cap = cv2.VideoCapture(r"C:\Users\suley\Desktop\software\materials\opencv_materials\hsv.mp4")
# cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)

# webcamdan yapilmak istenirse 0 yazilmasi yeterli olacaktir
cv2.namedWindow("trackbar")

cv2.createTrackbar("lh", "trackbar", 0, 179, nothing)  # trackbarlar olusturuldu
cv2.createTrackbar("ls", "trackbar", 0, 255, nothing)
cv2.createTrackbar("lv", "trackbar", 0, 255, nothing)
cv2.createTrackbar("uh", "trackbar", 0, 179, nothing)
cv2.createTrackbar("us", "trackbar", 0, 255, nothing)
cv2.createTrackbar("uv", "trackbar", 0, 255, nothing)

cv2.setTrackbarPos("uh", "trackbar", 179)  # trackbarlarin varsayilan degerleri belirlendi
cv2.setTrackbarPos("us", "trackbar", 255)
cv2.setTrackbarPos("uv", "trackbar", 255)

while True:
    ret, frame = cap.read()

    if ret == 0:
        break

    r, c, hc = frame.shape
    frame = cv2.resize(frame, (int(c/3), int(r/3)))
    frame_contours = frame.copy()

    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    lh = cv2.getTrackbarPos("lh", "trackbar")
    ls = cv2.getTrackbarPos("ls", "trackbar")
    lv = cv2.getTrackbarPos("lv", "trackbar")
    uh = cv2.getTrackbarPos("uh", "trackbar")
    us = cv2.getTrackbarPos("us", "trackbar")
    uv = cv2.getTrackbarPos("uv", "trackbar")

    lower_blue = np.array([lh, ls, lv])  # upper ve lower hsv renk degerleri ile tek boyutlu dizi olusturulması saglandi
    upper_blue = np.array([uh, us, uv])

    mask = cv2.inRange(hsv, lower_blue, upper_blue)  # girilen degerler arasindaki rengin secilmesi saglandi

    bitwise = cv2.bitwise_and(frame, frame, mask=mask)  # siyah 1 beyaz 0'dir bitwise ile belirlenen nesne onplana cikti

    kernel = np.ones((5, 5), np.uint8)
    dilation = cv2.dilate(mask, kernel, iterations=2)
    blur = cv2.GaussianBlur(dilation, (5, 5), 1)
    cnt, _ = cv2.findContours(blur, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    cv2.drawContours(frame_contours, cnt, 0, (0, 255, 0), 2)
    cv2.imshow("dilate", dilation)
    cv2.imshow("blur", blur)
    cv2.imshow("contours", frame_contours)

    cv2.imshow("frame", frame)
    cv2.imshow("mask", mask)
    cv2.imshow("bitwise",bitwise)

    if cv2.waitKey(50) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()
