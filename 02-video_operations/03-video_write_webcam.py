import cv2

cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)  # goruntu webcamdan alinmak uzere ayarlandi

filename = r"C:\Users\suley\Desktop\software\materials\opencv_materials\video_write.avi"  # dosya adi belirlendi
codec = cv2.VideoWriter_fourcc("W", "M", "V", "2")  # kodekler belirlendi
frame_rate = 500  # frame hızı belirlendi. ne kadar fazla olursa o kadar hizli olur
resolution = (640, 480)  # video pencere boyutu belirlendi

video_file = cv2.VideoWriter(filename, codec, frame_rate, resolution)  # videonun yazilmasi icin fonksiyon kullanildi

while True:

    ret, frame = cap.read()
    if ret == 0:
        break

    video_file.write(frame)  # her bir frame videoya yazilmak uzere gonderildi

    frame = cv2.flip(frame, 1)

    cv2.imshow("frame", frame)
    if cv2.waitKey(10) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()
