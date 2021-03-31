import cv2

cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)

genislik = cap.get(3)  # get(3) ile genislik degeri 4 ile de yukseklik degeri float olarak bulundu
yukseklik = cap.get(4)

print(genislik)
print(yukseklik)

cap.set(3, genislik*2)  # set ile istenilen aralik yeniden boyutlandirildi
cap.set(4, yukseklik*2)

genislik = cap.get(3)
yukseklik = cap.get(4)

print(genislik)
print(yukseklik)

while True:
    ret, frame = cap.read()

    if ret == 0:
        break

    frame = cv2.flip(frame, 1)

    cv2.imshow("frame", frame)

    if cv2.waitKey(5) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()
