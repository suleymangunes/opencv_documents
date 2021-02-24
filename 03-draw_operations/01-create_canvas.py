import cv2
import numpy as np

canvas = np.zeros((512, 512, 3), np.uint8)  # sifirlardan olusan numpy dizisi ile tuval olusturuldu.
# par1 ilk iki deger tuval boyutunu belirledi, 3. deger tuvalin renklendirilme ozelligini aktif kıldı
# par3 degerlerin 8 bytlik sinirda kalmasini sagladi.

canvas_white = np.zeros((512, 512, 3), np.uint8) + 255  # + 255 ile tuvalin beyaz olmasi saglandi

cv2.imshow("canvas white", canvas_white)
cv2.imshow("canvas black", canvas)
cv2.waitKey(0)
cv2.destroyAllWindows()
