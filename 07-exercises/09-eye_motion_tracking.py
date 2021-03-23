import cv2

cap = cv2.VideoCapture(r"C:\Users\suley\Desktop\software\materials\opencv_materials\eye.mp4")

while True:

    ret, frame = cap.read()

    if ret == 0:
        break

    roi = frame[80:220, 250:450]  # gozbebeginin bulundugu alan secildi
    rows, cols, color = roi.shape  # secilen alanin boyutu degiskenlere atandi

    gray = cv2.cvtColor(roi, cv2.COLOR_BGRA2GRAY)  # roi alani gri tonlarina donusturuldu

    _, thresh = cv2.threshold(gray, 0.001, 255, cv2.THRESH_BINARY_INV)  # roi alani bulunan renk degerlerinde esik
    # degerine gore siyah ve beyaz formatina donusturuldu

    contours, _c = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)  # konturler bulundu

    contours = sorted(contours, key=lambda x: cv2.contourArea(x), reverse=True)
    # konturler alanlarina gore buyukten kucuge dogru siralandi

    for cnt in contours:  # her bir kontor icerisinde donuldu ancak sadece en buyuk olan ile islem yapildi
        (x, y, w, h) = cv2.boundingRect(cnt)  # en buyuk kontor baslangic sol ust noktasinin x ve y koordinati
        # genislik ve yuksekligi degiskenlere atandi

        cv2.circle(roi, (x + int(w / 2), y + int(h / 2)), 20, (0, 0, 255), 2)  # belirlenen bolgeyi kaplayacak dortgen cizildi
        cv2.line(roi, (x + int((w / 2)), 0), (x + int((w / 2)), rows), (0, 255, 0), 1)
        # baslangic noktasina genisligin yarisi eklenerek x duzlem merkezinden gecen cizgi cizildi
        cv2.line(roi, (0, y + int((h / 2))), (cols, y + int((h / 2))), (0, 255, 0), 1)
        # baslangic noktasina yuksekligin yarisi eklenerek y duzlem merkezinden gecen cizgi cizildi

        break

    cv2.imshow("frame", frame)
    # cv2.imshow("thresh", thresh)
    # cv2.imshow("roi", roi)
    if cv2.waitKey(80) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()
