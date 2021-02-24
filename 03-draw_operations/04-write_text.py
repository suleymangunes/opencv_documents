import cv2
import numpy as np

can = np.zeros((500, 1200, 3), dtype=np.uint8)  # tuval olusturuldu

text = "The Godfather"  # yazi belirlendi
font = cv2.FONT_HERSHEY_SIMPLEX  # font belirlendi

cv2.putText(can, text, (45, 290), font, 5, (0, 255, 255), 7)  # yazi tuvale eklendi. par1 tuval, par2 yazi,
# par3 yazinin baslangic noktasi, par4 yazinin fontu, par5 font buyuklugu, par6 yazi rengi, par7 yazi kalinligi

cv2.imshow("tuval", can)
cv2.waitKey(0)
cv2.destroyAllWindows()
