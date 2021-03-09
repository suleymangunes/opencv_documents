import cv2
import numpy as np

vid = cv2.VideoCapture(r"C:\Users\suley\Desktop\software\materials\opencv_materials\line.mp4")

while True:
    ret, frame = vid.read()
    if ret == 0:
        break
    frame = cv2.resize(frame, (640, 480))  # boyut ayarlandi
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)  # renk degeri hsv'ye donusturuldu

    lower_yellow = np.array([18, 94, 140], np.uint8)  # hsv renk araligi belirlendi
    upper_yellow = np.array([48, 255, 255], np.uint8)

    mask = cv2.inRange(hsv, lower_yellow, upper_yellow)  # maskeleme islemi yapildi
    edges = cv2.Canny(mask, 75, 250)  # maskeleme uzerinden kenarlar belirlendi

    lines = cv2.HoughLinesP(edges, 1, np.pi/180, 50, maxLineGap=50)  # hough ile cizgiler belirlendi

    try:  # try except ile cizgi bulundugu surece kod calismasi saglandi
        for i in lines:  # cizgiler oldugu surece donen dongu saglandi
            (x1, y1, x2, y2) = i[0]  # baslangic bitis koordinat degerleri atandi
            cv2.line(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)  # cizgi cizildi
    except:  # cizgi bitince videonun sonlandirilmasi saglandi
        break

    cv2.imshow("frame", frame)

    if cv2.waitKey(5) & 0xFF == ord("q"):
        break

vid.release()
cv2.destroyAllWindows()
