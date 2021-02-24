import cv2

cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)  # par1 0 degeri ile webcamdan video okunmasi saglandi

while True:

    ret, frame = cap.read()  # read methodu videoyu 2 degiskene ayirdi

    if ret == 0:  # ret kare degeri icin true false donderir. eger 0 ise donguden cikilmasi saglandi
        break

    frame = cv2.flip(frame, 1)  # karelerin y ekseninde dondurulmesi saglandi. amac ayna goruntusu
    # par2 ile farkli eksenlere gore de islemler yapilabilir3

    cv2.imshow("frame", frame)

    if cv2.waitKey(10) & 0xFF == ord("q"):  # her kare arasina 10 milisaniye birakildi q'ya basilinca cikmasi saglandi
        break

cap.release()
cv2.destroyAllWindows()
