import cv2

cap = cv2.VideoCapture(r"C:\Users\suley\Desktop\software\materials\opencv_materials\video.mp4")

while True:
    ret, frame = cap.read()

    if ret == 0:
        break

    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # her bir frame'in renk formati degistirilerek videoda renk formati degisimi saglandi

    cv2.imshow("frame", frame)

    if cv2.waitKey(30) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()
