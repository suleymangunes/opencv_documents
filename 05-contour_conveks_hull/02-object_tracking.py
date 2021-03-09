import cv2
import numpy as np

cap = cv2.VideoCapture(r"C:\Users\suley\Desktop\software\materials\opencv_materials\dog.mp4")

while True:
    ret, frame = cap.read()
    if ret == 0:
        break

    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)  # karedeki renk degeri hsv formatina donusturuldu

    lower_white = np.array([0, 0, 240])  # bulunacak nesnenin rengine ozel hsv kodlari belirlendi
    upper_white = np.array([255, 15, 255])

    mask = cv2.inRange(hsv, lower_white, upper_white)  # maskeleme islemi yapildi
    res = cv2.bitwise_and(frame, frame, mask=mask)

    cv2.imshow("original", frame)
    cv2.imshow("mask", mask)
    cv2.imshow("res", res)

    if cv2.waitKey(5) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()
