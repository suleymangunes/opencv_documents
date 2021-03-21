# gereksiz sekilde ilk frame alindi diff ile aralarindaki fark saptandi
# goruntu yumusatildi ve threshold uygulandi

import cv2

cap = cv2.VideoCapture(r"C:\Users\suley\Desktop\software\materials\opencv_materials\car.mp4")
_, first_frame = cap.read()
r, c, hc = first_frame.shape
first_frame = cv2.resize(first_frame, (int(c / 2), int(r / 2)))

first_gray = cv2.cvtColor(first_frame, cv2.COLOR_BGR2GRAY)
first_gray = cv2.GaussianBlur(first_gray, (5, 5), 0)

while True:
    ret, frame = cap.read()

    if ret == 0:
        break
    r1, c1, hc1 = frame.shape
    frame = cv2.resize(frame, (int(c1 / 2), int(r1 / 2)))

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    gray = cv2.GaussianBlur(gray, (5, 5), 0)

    diff = cv2.absdiff(first_gray, gray)
    _, diff = cv2.threshold(diff, 25, 255, cv2.THRESH_BINARY)

    if ret == 0:
        break

    cv2.imshow("frame", frame)
    cv2.imshow("first frame", first_frame)
    cv2.imshow("diff", diff)

    if cv2.waitKey(20) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()
