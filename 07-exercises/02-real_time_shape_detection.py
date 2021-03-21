import cv2
import numpy as np


def nothing(x):
    pass


font = cv2.FONT_HERSHEY_SIMPLEX

cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
cv2.namedWindow("setting")

cv2.createTrackbar("lower hue", "setting", 0, 180, nothing)
cv2.createTrackbar("lower saturation", "setting", 0, 255, nothing)
cv2.createTrackbar("lower value", "setting", 0, 255, nothing)
cv2.createTrackbar("upper hue", "setting", 0, 180, nothing)
cv2.createTrackbar("upper saturation", "setting", 0, 255, nothing)
cv2.createTrackbar("upper value", "setting", 0, 255, nothing)


while True:

    ret, frame = cap.read()
    frame = cv2.flip(frame, 1)
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    lh = cv2.getTrackbarPos("lower hue", "setting")
    ls = cv2.getTrackbarPos("lower saturation", "setting")
    lv = cv2.getTrackbarPos("lower value", "setting")
    uh = cv2.getTrackbarPos("upper hue", "setting")
    us = cv2.getTrackbarPos("upper saturation", "setting")
    uv = cv2.getTrackbarPos("upper value", "setting")

    lower_hsv = np.array([lh, ls, lv])
    upper_hsv = np.array([uh, us, uv])

    mask = cv2.inRange(hsv, lower_hsv, upper_hsv)
    kernel = np.ones((5, 5), np.uint8)
    mask = cv2.erode(mask, kernel)

    contour, _ = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    for cnt in contour:
        area = cv2.contourArea(cnt)  # geometrik sekillerin alanlari bulundu
        epsilon = 0.02 * cv2.arcLength(cnt, True)  # cevre uzerinden hesap yapilarak epsilon degiskenine deger atandi
        approx = cv2.approxPolyDP(cnt, epsilon, True)  # bulunan deger ile her geomterik seklin kosegen koordinatlari
        # 2 boyutlu olarak degiskene gonderildi

        x = approx.ravel()[0]
        y = approx.ravel()[1]

        if area > 150:  # ala boyutu belirli olan degerlerin sadece dikkate alinmasi saglandi
            cv2.drawContours(frame, [approx], 0, (0, 0, 0), 5)  # konturler cizildi
            if len(approx) == 3:
                cv2.putText(frame, "triangle", (x, y), font, 1, (0, 0, 0))
            if len(approx) == 4:
                cv2.putText(frame, "rectangle", (x, y), font, 1, (0, 0, 0))

    cv2.imshow("frame", frame)
    cv2.imshow("mask", mask)

    if cv2.waitKey(5) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()
