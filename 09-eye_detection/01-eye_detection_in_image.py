import cv2

img = cv2.imread(r"C:\Users\suley\Desktop\software\materials\opencv_materials\face.png")
cascade_face = cv2.CascadeClassifier(r"C:\Users\suley\Desktop\software\materials\opencv_materials\frontalface.xml")
cascade_eye = cv2.CascadeClassifier(r"C:\Users\suley\Desktop\software\materials\opencv_materials\eye.xml")
# once yuz bulunup daha sonra yuz alani icinde goz bulunmasi icin cascadeler eklendi

gray = cv2.cvtColor(img, cv2.COLOR_BGRA2GRAY)  # resim gri formata donusturuldu
faces = cascade_face.detectMultiScale(gray, 1.3, 7)  # yuz degerleri bulundu

for (x, y, w, h) in faces:  # bulunan yuz degerleri arasinda donerek ekrana dortgen cizildi
    cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 2)

roi_face = img[y : y + h, x : x + w]  # yuz degeri roi icine alindi
roi_gray = gray[y : y + h, x : x + w]

eyes = cascade_eye.detectMultiScale(roi_gray)  # roi icerisinde gozler arandi

for (xe, ye, we, he) in eyes:  # bulunan gozler arasinda donulerek ekrana dortgen cizildi
    cv2.rectangle(roi_face, (xe, ye), (xe + we, ye + he), (0, 255, 0), 2)

cv2.imshow("image", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
