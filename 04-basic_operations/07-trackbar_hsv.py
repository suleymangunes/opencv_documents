import cv2  # opencv kutuphanesi ice aktarildi
import numpy as np  # numpy kutuphanesi ice aktarildi

cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)  # webcamdan video okunmasi saglandi


def nothing(x):  # trackbar calismasi icin varsayilan bos fonksiyon tanimlandi
    pass


cv2.namedWindow("trackbar")  # tracbar icin pencere olusturuldu
cv2.resizeWindow("trackbar", 500, 500)  # trackbar penceresi yeniden boyutlandirildi

cv2.createTrackbar("lover-h", "trackbar", 0, 180, nothing)  # hsv renk kodlarinin lover deger araliklari icin trackbar
cv2.createTrackbar("lover-s", "trackbar", 0, 255, nothing)  # olusturuldu. pencereye atandi, min ve max degerler
cv2.createTrackbar("lover-v", "trackbar", 0, 255, nothing)  # belirlendi. varsayilan fonksiyon gonderildi

cv2.createTrackbar("upper-h", "trackbar", 0, 180, nothing)  # lover degerler icin yapilanlar upper degerler icin de
cv2.createTrackbar("upper-s", "trackbar", 0, 255, nothing)  # yapildi
cv2.createTrackbar("upper-v", "trackbar", 0, 255, nothing)

cv2.setTrackbarPos("upper-h", "trackbar", 180)  # tracbar degerlerine varsayilan degerler atandi
cv2.setTrackbarPos("upper-s", "trackbar", 255)
cv2.setTrackbarPos("upper-v", "trackbar", 255)

while True:
    ret, frame = cap.read()  # webcamdan gelen her kare degerlere atandi

    frame = cv2.flip(frame, 1)  # gelen goruntunun y eksenine gore simetrisi alindi

    frame_hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)  # kare hsv formatina donusturuldu amac hsv renk araliklarini
    # belirken degerleri buna uygun kareye yazmak

    l_h = cv2.getTrackbarPos("lover-h", "trackbar")  # trackbarlarin anlik degeri alindi
    l_s = cv2.getTrackbarPos("lover-s", "trackbar")
    l_v = cv2.getTrackbarPos("lover-v", "trackbar")

    u_h = cv2.getTrackbarPos("upper-h", "trackbar")
    u_s = cv2.getTrackbarPos("upper-s", "trackbar")
    u_v = cv2.getTrackbarPos("upper-v", "trackbar")

    lover_color = np.array([l_h, l_s, l_v])  # anlik degerler listeye atandi
    upper_color = np.array([u_h, u_s, u_v])

    mask = cv2.inRange(frame_hsv, lover_color, upper_color)  # alinan degerler ile maskeleme katmani olusturuldu

    cv2.imshow("original", frame)  # orijinal pencere gosterildi
    cv2.imshow("mask", mask)  # maskelenmis pencere gosterildi

    if cv2.waitKey(20) & 0xFF == ord("q"):  # kare arasi gecis hizi belirlendi ve q ya basilira cikilmasi saglandi
        break

cap.release()  # webcamdan alinan goruntu serbest birakildi
cv2.destroyAllWindows()  # pencerelerin serbest birakilmasi saglandi
