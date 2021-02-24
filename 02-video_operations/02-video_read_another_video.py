import cv2

cap = cv2.VideoCapture(r"C:\Users\suley\Desktop\software\materials\opencv_materials\video.mp4")

while True:  # videonun her karesinde donecek fonksiyon tanimlandi

    ret, frame = cap.read()  # cap okununca ret ve frame olarak iki degiskene ayrildi

    if ret == 0:  # eger ret sifi ise donguden cikilmasi saglandi
        break

    cv2.imshow("frame", frame)

    if cv2.waitKey(10) & 0xFF == ord("q"):
        break


cap.release()
cv2.destroyAllWindows()