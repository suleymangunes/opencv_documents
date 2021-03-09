import cv2

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()

    # frame = cv2.flip(frame, 1)

    edges = cv2.Canny(frame, 100, 150)  # kenarlar belirlendi par1 goruntuyu aldi, par 2 kenarlar arasi uzaklik
    # par3 kenar bulma ayrintisi

    cv2.imshow("webcam", frame)
    cv2.imshow("edges", edges)

    if cv2.waitKey(5) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()
