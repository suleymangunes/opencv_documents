import cv2

cap = cv2.VideoCapture(r"C:\Users\suley\Desktop\software\materials\opencv_materials\traffic.mp4")

subtractor = cv2.createBackgroundSubtractorMOG2(history=100, varThreshold=300, detectShadows=False)
# goruntudeki araclari bulan fonksiyon tanimlandi

while True:

    ret, frame = cap.read()
    if ret == 0:
        break
    frame = cv2.resize(frame, (640, 480))

    mask = subtractor.apply(frame)  # fonksiyon her kare uzerinde uygulandi ve sonuclar imshow gosterildi

    cv2.imshow("frame", frame)
    cv2.imshow("mask", mask)

    if cv2.waitKey(20) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()
