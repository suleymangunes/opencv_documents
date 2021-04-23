import cv2

cap = cv2.VideoCapture(r"C:\Users\suley\Desktop\software\materials\opencv_materials\video.mp4")
circles = []  # cember koordinatlarini alacak bos liste tanimlandi


def mouse(event, x, y, flags, params):  # farede sag tusa tiklandiginda o anki koordinati donduren fonskiyon tanimlandi
    if event == cv2.EVENT_LBUTTONDOWN:  # sag tusa basilinca bos listeye koordinatlar tupple olarak gonderildi
        circles.append((x, y))
        print(x, y)


cv2.namedWindow("frame")  # mouse islevinin caliacagi pencere tanimlandi
cv2.setMouseCallback("frame", mouse)  # pencere uzerinde mouse hareketleri

while True:
    ret, frame = cap.read()

    if ret == 0:
        break

    for c in circles:  # circle listesi icindeki cemberler cizildi
        cv2.circle(frame, c, 20, (0, 255, 0), -1)

    cv2.imshow("frame", frame)
    key = cv2.waitKey(100)
    if key == 27:
        break
    elif key == ord("c"):  # c tusuna basilinca listenin temizlenmesi saglandi
        circles = []

cap.release()
cv2.destroyAllWindows()
