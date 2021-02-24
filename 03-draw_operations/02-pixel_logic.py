import cv2
import numpy as np  # numpy modulu ice aktarildi

can = np.zeros((10, 10, 3), np.uint8)  # numpy ile her pikselin renginin siyah oldugu renklendirilebir tuval olusturuldu
can_bw = np.zeros((10, 10), np.uint8)  # renklendirilemez tuval olusturuldu (siyah ve beyaz tonlari sadece)

can[0, 0] = (255, 255, 255)  # belirli noktalardaki piksellerin renk kodu degistirildi
can[0, 1] = (255, 255, 200)
can[0, 2] = (255, 255, 150)
can[0, 3] = (255, 255, 100)
can[0, 4] = (255, 255, 50)

can_bw[0, 0] = 255  # belirli noktalardaki piksellerin renk kodu degistirildi
can_bw[0, 1] = 200
can_bw[0, 2] = 150
can_bw[0, 3] = 100
can_bw[0, 4] = 50

can = cv2.resize(can, (500, 500), interpolation=cv2.INTER_AREA)  # pencereler tekrar boyutlandirildi
can_bw = cv2.resize(can_bw, (500, 500), interpolation=cv2.INTER_AREA)

cv2.imshow("canvas color", can)
cv2.imshow("canvas no color", can_bw)

cv2.waitKey(0)
cv2.destroyAllWindows()
