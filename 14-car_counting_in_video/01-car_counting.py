import cv2

vid = cv2.VideoCapture(r"C:\Users\suley\Desktop\software\materials\opencv_materials\traffic2.avi")
backsub = cv2.createBackgroundSubtractorMOG2()  # arka plani temizleyen fonksiyon degiskene tanimlandi
c = 0  # arac sayisini sayacak sayac tanimlandi

while True:
    ret, frame = vid.read()
    if ret == 0:
        break

    fgmask = backsub.apply(frame)  # arka plan temizleyen fonksiyon uygulandi
    cv2.line(frame, (50, 0), (50, 300), (0, 0, 255), 2)  # ekranda arac gecerken saymasi icin duz 2 cizgi cizildi
    cv2.line(frame, (150, 0), (150, 300), (0, 0, 255), 2)

    contours, hierarchy = cv2.findContours(fgmask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    # kontur degerleri bulundu

    try:  # hierarchy degerleri hata vermesin diye try except blogu kullanildi
        hierarchy = hierarchy[0]
    except:
        hierarchy = []

    for contour in contours:  # kontur degerleri icinde donen dongu tanimlandi
        (x, y, w, h) = cv2.boundingRect(contour)  # konturleri saran dortgenler bulundu
        if w > 40 and h > 40:  # eger dortgen degerleri belirli buyuklukte ise konturu saran dortgen cizildi
            cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 3)
            if x > 50 and x < 70:  # eger sol ust kose koordinati belirlenen alan icerisine girdiyse c artirildi
                c += 1

    cv2.putText(frame, "car: "+str(c), (90, 100), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 255, 0), 3)

    cv2.imshow("frame", frame)
    if cv2.waitKey(20) & 0xFF == ord("q"):
        break

vid.release()
cv2.destroyAllWindows()
