import cv2
import numpy as np
import math


def find_max_contour(contours):  # roideki seklin uc noktalarini indislerini bulan fonksiyon tanimlandi
    max_i = 0  # uc noktalarin indisini tutan degisken tanimlandi
    max_area = 0  # roideki nesneler icinde maximum alan degerini tutacak degisken tanimlandi (amac sadece eli bulmasi)

    for i in range(len(contours)):  # kontur sayisi kadar dongude donulmesi saglandi
        area_hand = cv2.contourArea(contours[i])  # her karede her kontur degeri icin alanlar bulundu

        if max_area < area_hand:  # max alanin indis degerini tutacak kosul tanimlandi
            max_area = area_hand  # alani en buyuk olan contour degeri kosula bagli bulundu
            max_i = i  # bulunan en buyuk alanli nesne yani sadece elin uc nokta indisleri degiskene atandi

    try:  # eger roide el bulunmazsa hata vermemesi icin try except blogu tanimlandi
        c = contours[max_i]  # yeni c degeri elin alaninin bulundugu indis noktasindaki kontur degeri olarak tanimlandi
        # yani bir karede sadece elin kontur degeri alinmasi saglandi
    except:
        contours = [0]  # eger bulamazsa degerin sifir olmasi saglandi
        c = contours[0]

    return c


cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)  # webcamdan goruntu alindi

while True:
    ret, frame = cap.read()  # kareler okundu

    if ret == 0:  # eger kare kalmadiysa donguden cikilmasi saglandi
        break

    frame = cv2.flip(frame, 1)  # karelerin y eksenine gore yansimasi alindi

    roi = frame[100:370, 200:400]  # ekranin belirli bolgesi secildi (sadece el ile ilgilenildigi icin yuz kadar alan)
    cv2.rectangle(frame, (200, 100), (400, 370), (0, 0, 255), 0)

    hsv = cv2.cvtColor(roi, cv2.COLOR_BGR2HSV)  # elin icinde bulundugu aralik hsv formatina donusturuldu
    lower_color = np.array([0, 45, 79], dtype=np.uint8)  # ten rengine yakin hsv formatindaki alt degerler alindi
    upper_color = np.array([17, 255, 255], dtype=np.uint8)  # ust degerlerde alinip tek boyutlu dizi icine yerlestirildi

    mask = cv2.inRange(hsv, lower_color, upper_color)  # degerler ile maskeleme islemi yapildi
    # sadece ten rengindeki goruntu ekranda secilmis oldu

    kernel = np.ones((5, 5), np.uint8)  # beyaz noktalari kalinlastiracak fonksiyon icin cekirdek olusturuldu
    mask = cv2.dilate(mask, kernel, iterations=1)  # beyaz noktalarin daha da kalinalastirilmasi saglandi
    mask = cv2.medianBlur(mask, 21)  # siyah puruzlerin kaybolmasi icin resim yumusatildi

    contours, _ = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)  # roide konturler bulundu

    if len(contours) > 0:

        c = find_max_contour(contours)  # konturler icerisinde uc noktalarin indislerini bulacak fonksiyon tanimlandi

        # yeni c degeri karede her konturu degil sadece elin kontur degerlerini icerir

        extLeft = tuple(c[c[:, :, 0].argmin()][0])
        # elin kontor degerleri arasinda en solda bulunan tum kontur degerleri icerisinde en kucuk olanin indisi alindi
        # bulunan indis noktasindan en soldaki degerin koordinatlari bulunmasi saglandi
        extRight = tuple(c[c[:, :, 0].argmax()][0])  # ayni islemler diger degerler icin de tekrarlandi
        extTop = tuple(c[c[:, :, 1].argmin()][0])

        cv2.circle(roi, extLeft, 5, (0, 255, 0), 2)  # bulunan her uc noktalar uzerinde cember cizildi
        cv2.circle(roi, extRight, 5, (0, 255, 0), 2)
        cv2.circle(roi, extTop, 5, (0, 255, 0), 2)

        cv2.line(roi, extLeft, extTop, (255, 0, 0), 2)  # cemberler arasi cizgi cizilmesi saglandi
        cv2.line(roi, extTop, extRight, (255, 0, 0), 2)
        cv2.line(roi, extRight, extLeft, (255, 0, 0), 2)

        # iki nokta arasinda analitik geometri formulunden yararlanarak istenilen kosenin komsu kenaralari ve
        # karsisindaki kenarin uzunlugu bulunmus oldu
        a = math.sqrt((extRight[0] - extTop[0]) ** 2 + (extRight[1] - extTop[1]) ** 2)
        b = math.sqrt((extRight[0] - extLeft[0]) ** 2 + (extRight[1] - extLeft[1]) ** 2)
        c = math.sqrt((extTop[0] - extLeft[0]) ** 2 + (extTop[1] - extLeft[1]) ** 2)

        try:
            angle_ab = int(math.acos((a ** 2 + b ** 2 - c ** 2) / (2 * b * c)) * 57)
            # uc kenari bilinen ucgende aci bulma formulu ile istenilen kosedeki aci bulundu

            cv2.putText(roi, str(angle_ab), (extRight[0] - 100 + 50, extRight[1]), cv2.FONT_HERSHEY_SIMPLEX, 1,
                        (0, 0, 255), 2, cv2.LINE_AA)  # aci degeri yazdirildi
        except:
            cv2.putText(roi, " ? ", (extRight[0] - 100 + 50, extRight[1]), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2,
                        cv2.LINE_AA)  # eger aci bulunmazsa ? karakterini gonderilmesi saglandi

    cv2.imshow("frame", frame)
    # cv2.imshow("roi", roi)
    # cv2.imshow("mask", mask)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()
