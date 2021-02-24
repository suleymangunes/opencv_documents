import cv2

img = cv2.imread(r"C:\Users\suley\Desktop\software\materials\opencv_materials\resim.jpg")


def resize_with_aspect_ratio(image, width=None, height=None, inter=cv2.INTER_AREA):
    # yeniden boyutlandirma icin fonksiyon tanimlandi

    h, w, c = image.shape

    if width is None and height is None:  # yeni degerler yok ise boyutlandirma yapilmadi
        return image

    elif width is None:  # genislik yok ise yeni yukseklik degeri eski degere bolundu bu sayede oran katsayisi olustu
        r = height / float(h)
        dimension = (int(w*r), height)  # katsayi ile yeni boyutlar belirlendi

    else:
        r = width / float(w)
        dimension = (width, int(h*r))

    return cv2.resize(image, dimension, interpolation=inter)  # sonuc fonksiyon sonunda yeniden boyutlandirildi


img2 = resize_with_aspect_ratio(img, width=None, height=600, inter=cv2.INTER_AREA)  # fonksiyon icin degerler gonderildi

cv2.imshow("original", img)
cv2.imshow("resize", img2)

cv2.waitKey(0)
cv2.destroyAllWindows()
