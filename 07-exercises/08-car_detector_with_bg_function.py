import cv2
import numpy as np

cap = cv2.VideoCapture(r"C:\Users\suley\Desktop\software\materials\opencv_materials\car4.mp4")

subtractor = cv2.createBackgroundSubtractorMOG2(history=100, varThreshold=300, detectShadows=False)
# fonksiyon ile arka plan cikarilmasi saglandi

while True:

    ret, frame = cap.read()
    if ret == 0:
        break
    frame = cv2.resize(frame, (640, 480))

    mask = subtractor.apply(frame)  # fonksiyon her kare uzerinde uygulandi

    kernel = np.ones((5, 10), np.uint8)  # her karede bulunan on plan degerlerini belirginlestirmede kullanilan
    mask = cv2.dilate(mask, kernel, iterations=1)  # fonksiyon icin cekirdek degeri olsuturuldu ve beyazlar kalilansti
    mask = cv2.medianBlur(mask, 15)  # beyazlar yumusatildi
    mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)  # siyah puruzlerin giderilmesi saglandi

    contours, _ = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)  # konturler bulundu

    for i in range(len(contours)):  # arka plana cizim yapilmasi icin dongu olusturuldu
        cv2.drawContours(frame, contours, i, (255, 0, 0), 4, 8)  # kontor degerleri cizildi
        # par3 kacinci kontorun cizilecegini belirtir

    cv2.imshow("frame", frame)
    cv2.imshow("mask", mask)

    if cv2.waitKey(20) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()
