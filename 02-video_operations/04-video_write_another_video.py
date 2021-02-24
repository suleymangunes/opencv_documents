import cv2

cap = cv2.VideoCapture(r"C:\Users\suley\Desktop\software\materials\opencv_materials\video.mp4")

file_name = r"C:\Users\suley\Desktop\software\materials\opencv_materials\video_yeniden.avi"
codec = cv2.VideoWriter_fourcc("W", "M", "V", "2")
frame_rate = 30
resolution = (1366, 720)
# dosya adi kodek degerleri kare hizi pencere boyutu tanimlandi

video_save = cv2.VideoWriter(file_name, codec, frame_rate, resolution)
# tanimlanan degerler ile video yazildi

while True:

    ret, frame = cap.read()

    if ret == 0:
        break

    video_save.write(frame)

    cv2.imshow("frame", frame)

    if cv2.waitKey(10) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()