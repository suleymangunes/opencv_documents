import cv2
import numpy as np

circles = []  # cember koordinatlarini alacak bos liste tanimlandi

img = cv2.imread(r"C:\Users\suley\Desktop\software\materials\opencv_materials\golgeler.jpg")
row, col, hc = img.shape
# img = cv2.resize(img, (int(col / 4), int(row / 4)))
r, c, h = img.shape
print("r", r)
print("c", c)
print("h", h)


def mouse(event, x, y, flags, params):  # farede sag tusa tiklandiginda o anki koordinati donduren fonskiyon tanimlandi
    if event == cv2.EVENT_LBUTTONDOWN:  # sag tusa basilinca bos listeye koordinatlar tupple olarak gonderildi
        circles.append((x, y))
        print(x, y)
        print(circles)


cv2.namedWindow("img")  # mouse islevinin caliacagi pencere tanimlandi
cv2.setMouseCallback("img", mouse)  # pencere uzerinde mouse hareketleri


cv2.imshow("img", img)
cv2.waitKey(0)
cv2.destroyAllWindows()

print(circles)

solust = np.array([[circles[0][0], circles[0][1]]])
sagust = np.array([[circles[1][0], circles[1][1]]])
solalt = np.array([[circles[2][0], circles[2][1]]])
sagalt = np.array([[circles[3][0], circles[3][1]]])

print("solust", solust)
print("sagust", sagust)
print("solalt", solalt)
print("sagalt", sagalt)

mypoints = np.array([solust, sagust, solalt, sagalt])
print(mypoints)
mypoints = np.float32(mypoints)
pts2 = np.float32([[0, 0], [891, 0], [0, 630], [891, 630]])
matrix = cv2.getPerspectiveTransform(mypoints, pts2)

dst = cv2.warpPerspective(img, matrix, (891, 630))

cv2.imshow("dst", dst)
cv2.waitKey(0)
cv2.destroyAllWindows()
