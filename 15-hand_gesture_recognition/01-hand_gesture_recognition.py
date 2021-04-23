import cv2
import numpy as np

vid = cv2.VideoCapture(0, cv2.CAP_DSHOW)
sayac = 0

while True:

    ret, frame = vid.read()

    frame = cv2.flip(frame, 1)
    kernel = np.ones((3, 3), np.uint8)

    roi = frame[101:200, 401:500]
    cv2.line(roi, (0, 49), (99, 49), 0, 2)
    cv2.rectangle(frame, (400, 100), (500, 200), (0, 0, 255), 0)

    hsv = cv2.cvtColor(roi, cv2.COLOR_BGR2HSV)

    lower_skin = np.array([0, 20, 70], dtype=np.uint8)
    upper_skin = np.array([20, 255, 255], dtype=np.uint8)

    mask = cv2.inRange(hsv, lower_skin, upper_skin)

    # mask = cv2.erode(mask, kernel)

    # mask = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel)
    mask = cv2.dilate(mask, kernel, iterations=4)

    mask = cv2.GaussianBlur(mask, (5, 5), 100)

    contours, _ = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    try:
        cv2.drawContours(roi, contours, -1, (0, 255, 0), 2)

        areas = [cv2.contourArea(c) for c in contours]
        max_index = np.argmax(areas)
        cnt = contours[max_index]
        x1, y1 = cnt[0][0][0], cnt[0][0][1]
        print("x1", x1)
        print("y1", y1)

        if y1 < 49:
            sayac += 1
            if sayac == 1:
                print("oldu")
        else:
            sayac = 0

        x, y, w, h = cv2.boundingRect(cnt)
        cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)
        cv2.circle(roi, (cnt[0][0][0], cnt[0][0][1]), 5, (0, 0, 255), -1)
    except:
        pass

    cv2.imshow("mask", mask)
    cv2.imshow("frame", frame)
    cv2.imshow("roi", roi)

    if cv2.waitKey(5) & 0xFF == ord("q"):
        break

vid.release()
cv2.destroyAllWindows()
