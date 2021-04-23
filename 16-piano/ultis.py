import cv2  # opencv modulu ice aktarildi
import numpy as np  # numpy modulu ice aktarildi
import pygame  # pygame modulu ice aktarildi
pygame.mixer.init()  # pygame ile sesler calinmasi icin mixer iceri alindi


def hsvbul():
    cap = cv2.VideoCapture(1, cv2.CAP_DSHOW)  # webcamdan video okunmasi saglandi


    def nothing(x):  # trackbar calismasi icin varsayilan bos fonksiyon tanimlandi
        pass


    cv2.namedWindow("trackbar")  # trackbar icin pencere olusturuldu
    cv2.resizeWindow("trackbar", 500, 500)  # trackbar penceresi yeniden boyutlandirildi

    cv2.createTrackbar("lover-h", "trackbar", 0, 180, nothing)
    cv2.createTrackbar("lover-s", "trackbar", 0, 255, nothing)  # olusturuldu. pencereye atandi, min ve max degerler
    cv2.createTrackbar("lover-v", "trackbar", 0, 255, nothing)  # belirlendi. varsayilan fonksiyon gonderildi
    cv2.createTrackbar("upper-h", "trackbar", 0, 180, nothing)  # lover degerler icin yapilanlar upper degerler icin de
    cv2.createTrackbar("upper-s", "trackbar", 0, 255, nothing)  # yapildi
    cv2.createTrackbar("upper-v", "trackbar", 0, 255, nothing)

    cv2.setTrackbarPos("upper-h", "trackbar", 180)  # tracbar degerlerine varsayilan degerler atandi
    cv2.setTrackbarPos("upper-s", "trackbar", 255)
    cv2.setTrackbarPos("upper-v", "trackbar", 255)

    while True:
        ret, frame = cap.read()  # webcamdan gelen her kare degerlere atandi
        frame = cv2.resize(frame, (960, 540))

        frame = cv2.flip(frame, 1)  # gelen goruntunun y eksenine gore simetrisi alindi

        frame_hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)  # kare hsv formatina donusturuldu amac hsv renk araliklarini

        l_h = cv2.getTrackbarPos("lover-h", "trackbar")  # trackbarlarin anlik degeri alindi
        l_s = cv2.getTrackbarPos("lover-s", "trackbar")
        l_v = cv2.getTrackbarPos("lover-v", "trackbar")
        u_h = cv2.getTrackbarPos("upper-h", "trackbar")
        u_s = cv2.getTrackbarPos("upper-s", "trackbar")
        u_v = cv2.getTrackbarPos("upper-v", "trackbar")

        lover_color = np.array([l_h, l_s, l_v])  # anlik degerler listeye atandi
        upper_color = np.array([u_h, u_s, u_v])

        mask_hsv = cv2.inRange(frame_hsv, lover_color, upper_color)  # alinan degerler ile maskeleme katmani olusturuldu

        cv2.imshow("original", frame)  # orijinal pencere gosterildi
        cv2.imshow("mask", mask_hsv)  # maskelenmis pencere gosterildi

        if cv2.waitKey(20) & 0xFF == ord("q"):  # kare arasi gecis hizi belirlendi ve q ya basilira cikilmasi saglandi
            break

    cap.release()  # webcamdan alinan goruntu serbest birakildi
    cv2.destroyAllWindows()  # pencerelerin serbest birakilmasi saglandi
    return lover_color, upper_color  # alt ve ust degerler donduruldu


def pers_noktalari():
    global matrix
    circles = []  # cember koordinatlarini alacak bos liste tanimlandi

    vid = cv2.VideoCapture(1, cv2.CAP_DSHOW)

    while True:
        ret, frame = vid.read()

        if ret == 0:
            break
        frame = cv2.resize(frame, (960, 540))
        frame = cv2.flip(frame, 1)

        def mouse(event, x, y, flags,
                  params):  # farede sag tusa tiklandiginda o anki koordinati donduren fonskiyon tanimlandi
            if event == cv2.EVENT_LBUTTONDOWN:  # sag tusa basilinca bos listeye koordinatlar tupple olarak gonderildi
                circles.append((x, y))
                print(x, y)
                print(circles)

        cv2.namedWindow("frame")  # mouse islevinin caliacagi pencere tanimlandi
        cv2.setMouseCallback("frame", mouse)  # pencere uzerinde mouse hareketleri

        try:
            for i in range(4):
                cv2.circle(frame, (circles[i]), 5, (0, 0, 255), 2)  # secilen noktada cember cizildi
        except Exception:
            pass

        cv2.imshow("frame", frame)

        if cv2.waitKey(1) & 0xFF == ord("q"):
            if len(circles) == 4:  # eger 4 nokta secildiyse perspektif uygulanmak uzere matrix hazirlandi
                solust = np.array([[circles[0][0], circles[0][1]]])
                sagust = np.array([[circles[1][0], circles[1][1]]])
                solalt = np.array([[circles[2][0], circles[2][1]]])
                sagalt = np.array([[circles[3][0], circles[3][1]]])
                mypoints = np.array([solust, sagust, solalt, sagalt])
                mypoints = np.float32(mypoints)
                pts2 = np.float32([[0, 0], [960, 0], [0, 540], [960, 540]])
                matrix = cv2.getPerspectiveTransform(mypoints, pts2)
                break
            else:  # eger 4 nokta yok ise tekrar secilmesi saglandi
                print("4 nokta sec")
                pers_noktalari()
    vid.release()
    cv2.destroyAllWindows()
    return matrix  # matric degeri pers icin gonderildi


def roi_noktalari(matrix):  # disardan alinan matrix degeri ile pers yapilan goruntude roi yani tus degerleri secildi
    roi_noktalar = []  # tuslarin merkezinde secilen noktalari tutacak liste tanimlandi
    cap = cv2.VideoCapture(1, cv2.CAP_DSHOW)

    while True:
        ret, frame = cap.read()

        if ret == 0:
            break
        frame = cv2.resize(frame, (960, 540))
        frame = cv2.flip(frame, 1)
        dst = cv2.warpPerspective(frame, matrix, (960, 540))

        def mouse(event, x, y, flags,
                  params):  # farede sag tusa tiklandiginda o anki koordinati donduren fonskiyon tanimlandi
            if event == cv2.EVENT_LBUTTONDOWN:
                roi_noktalar.append((x, y))
                print(x, y)
                print(roi_noktalar)

        cv2.namedWindow("dst")  # mouse islevinin caliacagi pencere tanimlandi
        cv2.setMouseCallback("dst", mouse)  # pencere uzerinde mouse hareketleri

        try:
            for i in range(25):
                cv2.circle(dst, (roi_noktalar[i]), 5, (0, 255, 0), 2)  # secilen her nokta icin cember cizildi
        except Exception:
            pass

        cv2.imshow("dst", dst)

        if cv2.waitKey(1) & 0xFF == ord("q"):
            if len(roi_noktalar) > 88:  # 88 tustan fazlasinin secilmemesi saglandi
                print("en fazla 88 tane sec.")
                roi_noktalari(matrix)  # eger daha fazla secildiyse fonksiyonun tekrar cagrilmasi saglandi
            break

    cap.release()
    cv2.destroyAllWindows()
    return roi_noktalar  # tuslarin merkez koordinatlarini tutan liste donderildi


def roi_dortgenleri(roilerim, dst):  # tuslarin oldugu degerler vs dst yani pers alinmis goruntu alindi
    for i in range(len(roilerim)):  # ver her nokta icin dortgen cizilmesi saglandi
        cv2.rectangle(dst, (roilerim[i][0] - 20, roilerim[i][1] - 30),  # roi buyuklugunde
                      (roilerim[i][0] + 20, roilerim[i][1] + 30), (255, 0, 0), 2)


# def bottombul(dst, roilerim, deger, b1, low_hsv, up_hsv):  # disardan alinan degerler ile kontrol islemini yapan
#     try:  # ve ses donderen fonksiyon tanimlandi
#
#         roi = dst[deger[1] - 30: deger[1] + 30, deger[0] - 10: deger[0] + 10]  # disardan alinan degerle roi alindi
#         hsv = cv2.cvtColor(roi, cv2.COLOR_BGR2HSV)  # deger maskleme islemini saglamasi icin hsv formatina gecti
#
#         # hazir dosya ise renkler boyle kalsin
#         lower_skin = np.array([0, 96, 171], dtype=np.uint8)
#         upper_skin = np.array([20, 255, 255], dtype=np.uint8)
#         mask = cv2.inRange(hsv, lower_skin, upper_skin)
#
#         # her defasinda renk kodlari alinirsa bunu al
#         # mask = cv2.inRange(hsv, low_hsv, up_hsv)
#
#         kernel = np.ones((3, 3), np.uint8)
#         mask = cv2.dilate(mask, kernel, iterations=4)
#         mask = cv2.GaussianBlur(mask, (5, 5), 100)
#         contours, _ = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
#
#         cv2.drawContours(roi, contours, -1, (0, 255, 0), 2)  # kontorler bulundu ve cizildi
#
#         areas = [cv2.contourArea(c) for c in contours]  # alan olarak en buyuk alan alindi ve bu alanda en dipteki
#         min_index = np.argmax(areas)  # index bulundu
#         cnt = contours[min_index]
#         bottommost = tuple(cnt[cnt[:, :, 1].argmax()][0])
#         cv2.circle(roi, bottommost, 5, (0, 0, 255), -1)  # en dipteki kontur indexine cember cizildi
#
#         if bottommost[1] > 20:  # en dipteki index degeri secilen roinin ortasini gecerse
#             b1 += 1  # b degeri artirildi ( disardan ilk olarak t = 0 olarak alinmisti )
#
#             if b1 == 1:  # eger deger 1 ise
#                 if deger == roilerim[0]:  # degerin roilerdeki degerine gore ses calinmasi saglandi
#                     print("a0 - oldu")
#                     sound = pygame.mixer.Sound(r"C:\Users\suley\Desktop\software\materials\opencv_materials\denemepiano\a0.mp3")
#                     sound.play()
#                 elif deger == roilerim[1]:
#                     print("bb0 - oldu")
#                     sound = pygame.mixer.Sound(r"C:\Users\suley\Desktop\software\materials\opencv_materials\denemepiano\bb0.mp3")
#                     sound.play()
#                 elif deger == roilerim[2]:
#                     print("b0 - oldu")
#                     sound = pygame.mixer.Sound(r"C:\Users\suley\Desktop\software\materials\opencv_materials\denemepiano\b0.mp3")
#                     sound.play()
#                 elif deger == roilerim[3]:
#                     print("c1 - oldu")
#                     sound = pygame.mixer.Sound(r"C:\Users\suley\Desktop\software\materials\opencv_materials\denemepiano\c1.mp3")
#                     sound.play()
#                 elif deger == roilerim[4]:
#                     print("db1 - oldu")
#                     sound = pygame.mixer.Sound(r"C:\Users\suley\Desktop\software\materials\opencv_materials\denemepiano\db1.mp3")
#                     sound.play()
#                 elif deger == roilerim[5]:
#                     print("d1 - oldu")
#                     sound = pygame.mixer.Sound(r"C:\Users\suley\Desktop\software\materials\opencv_materials\denemepiano\d1.mp3")
#                     sound.play()
#                 elif deger == roilerim[6]:
#                     print("eb1 - oldu")
#                     sound = pygame.mixer.Sound(r"C:\Users\suley\Desktop\software\materials\opencv_materials\denemepiano\eb1.mp3")
#                     sound.play()
#                 elif deger == roilerim[7]:
#                     print("e1 - oldu")
#                     sound = pygame.mixer.Sound(r"C:\Users\suley\Desktop\software\materials\opencv_materials\denemepiano\e1.mp3")
#                     sound.play()
#                 elif deger == roilerim[8]:
#                     print("f1 - oldu")
#                     sound = pygame.mixer.Sound(r"C:\Users\suley\Desktop\software\materials\opencv_materials\denemepiano\f1.mp3")
#                     sound.play()
#                 elif deger == roilerim[9]:
#                     print("gb1 - oldu")
#                     sound = pygame.mixer.Sound(r"C:\Users\suley\Desktop\software\materials\opencv_materials\denemepiano\gb1.mp3")
#                     sound.play()
#                 elif deger == roilerim[10]:
#                     print("ab1 - oldu")
#                     sound = pygame.mixer.Sound(r"C:\Users\suley\Desktop\software\materials\opencv_materials\denemepiano\ab1.mp3")
#                     sound.play()
#                 elif deger == roilerim[11]:
#                     print("a1 - oldu")
#                     sound = pygame.mixer.Sound(r"C:\Users\suley\Desktop\software\materials\opencv_materials\denemepiano\a1.mp3")
#                     sound.play()
#                 elif deger == roilerim[12]:
#                     print("bb1 - oldu")
#                     sound = pygame.mixer.Sound(r"C:\Users\suley\Desktop\software\materials\opencv_materials\denemepiano\bb1.mp3")
#                     sound.play()
#                 elif deger == roilerim[13]:
#                     print("b1 - oldu")
#                     sound = pygame.mixer.Sound(r"C:\Users\suley\Desktop\software\materials\opencv_materials\denemepiano\b1.mp3")
#                     sound.play()
#                 elif deger == roilerim[14]:
#                     print("c2 - oldu")
#                     sound = pygame.mixer.Sound(r"C:\Users\suley\Desktop\software\materials\opencv_materials\denemepiano\c2.mp3")
#                     sound.play()
#                 elif deger == roilerim[15]:
#                     print("db2 - oldu")
#                     sound = pygame.mixer.Sound(r"C:\Users\suley\Desktop\software\materials\opencv_materials\denemepiano\db2.mp3")
#                     sound.play()
#                 elif deger == roilerim[16]:
#                     print("d2 - oldu")
#                     sound = pygame.mixer.Sound(r"C:\Users\suley\Desktop\software\materials\opencv_materials\denemepiano\d2.mp3")
#                     sound.play()
#                 elif deger == roilerim[17]:
#                     print("eb2 - oldu")
#                     sound = pygame.mixer.Sound(r"C:\Users\suley\Desktop\software\materials\opencv_materials\denemepiano\eb2.mp3")
#                     sound.play()
#                 elif deger == roilerim[18]:
#                     print("e2 - oldu")
#                     sound = pygame.mixer.Sound(r"C:\Users\suley\Desktop\software\materials\opencv_materials\denemepiano\e2.mp3")
#                     sound.play()
#                 elif deger == roilerim[19]:
#                     print("f2 - oldu")
#                     sound = pygame.mixer.Sound(r"C:\Users\suley\Desktop\software\materials\opencv_materials\denemepiano\f2.mp3")
#                     sound.play()
#                 elif deger == roilerim[20]:
#                     print("gb2 - oldu")
#                     sound = pygame.mixer.Sound(r"C:\Users\suley\Desktop\software\materials\opencv_materials\denemepiano\gb2.mp3")
#                     sound.play()
#                 elif deger == roilerim[21]:
#                     print("g2 - oldu")
#                     sound = pygame.mixer.Sound(r"C:\Users\suley\Desktop\software\materials\opencv_materials\denemepiano\g2.mp3")
#                     sound.play()
#                 elif deger == roilerim[22]:
#                     print("ab2 - oldu")
#                     sound = pygame.mixer.Sound(r"C:\Users\suley\Desktop\software\materials\opencv_materials\denemepiano\ab2.mp3")
#                     sound.play()
#                 elif deger == roilerim[23]:
#                     print("a2 - oldu")
#                     sound = pygame.mixer.Sound(r"C:\Users\suley\Desktop\software\materials\opencv_materials\denemepiano\a2.mp3")
#                     sound.play()
#                 elif deger == roilerim[24]:
#                     print("bb2 - oldu")
#                     sound = pygame.mixer.Sound(r"C:\Users\suley\Desktop\software\materials\opencv_materials\denemepiano\bb2.mp3")
#                     sound.play()
#                 elif deger == roilerim[25]:
#                     print("b2 - oldu")
#                     sound = pygame.mixer.Sound(r"C:\Users\suley\Desktop\software\materials\opencv_materials\denemepiano\b2.mp3")
#                     sound.play()
#                 elif deger == roilerim[26]:
#                     print("c3 - oldu")
#                     sound = pygame.mixer.Sound(r"C:\Users\suley\Desktop\software\materials\opencv_materials\Piano.ff.G5.mp3")
#                     sound.play()
#                 elif deger == roilerim[27]:
#                     print("db3 - oldu")
#                     sound = pygame.mixer.Sound(r"C:\Users\suley\Desktop\software\materials\opencv_materials\Piano.ff.G5.mp3")
#                     sound.play()
#                 elif deger == roilerim[28]:
#                     print("d3 - oldu")
#                     sound = pygame.mixer.Sound(r"C:\Users\suley\Desktop\software\materials\opencv_materials\Piano.ff.G5.mp3")
#                     sound.play()
#                 elif deger == roilerim[29]:
#                     print("eb3 - oldu")
#                     sound = pygame.mixer.Sound(r"C:\Users\suley\Desktop\software\materials\opencv_materials\Piano.ff.G5.mp3")
#                     sound.play()
#                 elif deger == roilerim[30]:
#                     print("e3 - oldu")
#                     sound = pygame.mixer.Sound(r"C:\Users\suley\Desktop\software\materials\opencv_materials\Piano.ff.G5.mp3")
#                     sound.play()
#                 elif deger == roilerim[31]:
#                     print("f3 - oldu")
#                     sound = pygame.mixer.Sound(r"C:\Users\suley\Desktop\software\materials\opencv_materials\Piano.ff.G5.mp3")
#                     sound.play()
#                 elif deger == roilerim[32]:
#                     print("gb3 - oldu")
#                     sound = pygame.mixer.Sound(r"C:\Users\suley\Desktop\software\materials\opencv_materials\Piano.ff.G5.mp3")
#                     sound.play()
#                 elif deger == roilerim[33]:
#                     print("g3 - oldu")
#                     sound = pygame.mixer.Sound(r"C:\Users\suley\Desktop\software\materials\opencv_materials\Piano.ff.G5.mp3")
#                     sound.play()
#                 elif deger == roilerim[34]:
#                     print("ab3 - oldu")
#                     sound = pygame.mixer.Sound(r"C:\Users\suley\Desktop\software\materials\opencv_materials\Piano.ff.G5.mp3")
#                     sound.play()
#                 elif deger == roilerim[35]:
#                     print("a3 - oldu")
#                     sound = pygame.mixer.Sound(r"C:\Users\suley\Desktop\software\materials\opencv_materials\Piano.ff.G5.mp3")
#                     sound.play()
#                 elif deger == roilerim[36]:
#                     print("bb3 - oldu")
#                     sound = pygame.mixer.Sound(r"C:\Users\suley\Desktop\software\materials\opencv_materials\Piano.ff.G5.mp3")
#                     sound.play()
#                 elif deger == roilerim[37]:
#                     print("b3 - oldu")
#                     sound = pygame.mixer.Sound(r"C:\Users\suley\Desktop\software\materials\opencv_materials\Piano.ff.G5.mp3")
#                     sound.play()
#                 elif deger == roilerim[38]:
#                     print("eb1 - oldu")
#                     sound = pygame.mixer.Sound(r"C:\Users\suley\Desktop\software\materials\opencv_materials\Piano.ff.G5.mp3")
#                     sound.play()
#                 elif deger == roilerim[39]:
#                     print("c4 - oldu")
#                     sound = pygame.mixer.Sound(r"C:\Users\suley\Desktop\software\materials\opencv_materials\Piano.ff.G5.mp3")
#                     sound.play()
#                 elif deger == roilerim[40]:
#                     print("db4 - oldu")
#                     sound = pygame.mixer.Sound(r"C:\Users\suley\Desktop\software\materials\opencv_materials\Piano.ff.G5.mp3")
#                     sound.play()
#                 elif deger == roilerim[41]:
#                     print("d4 - oldu")
#                     sound = pygame.mixer.Sound(r"C:\Users\suley\Desktop\software\materials\opencv_materials\Piano.ff.G5.mp3")
#                     sound.play()
#                 elif deger == roilerim[42]:
#                     print("eb4 - oldu")
#                     sound = pygame.mixer.Sound(r"C:\Users\suley\Desktop\software\materials\opencv_materials\Piano.ff.G5.mp3")
#                     sound.play()
#                 elif deger == roilerim[43]:
#                     print("e4 - oldu")
#                     sound = pygame.mixer.Sound(r"C:\Users\suley\Desktop\software\materials\opencv_materials\Piano.ff.G5.mp3")
#                     sound.play()
#                 elif deger == roilerim[44]:
#                     print("f4 - oldu")
#                     sound = pygame.mixer.Sound(r"C:\Users\suley\Desktop\software\materials\opencv_materials\Piano.ff.G5.mp3")
#                     sound.play()
#                 elif deger == roilerim[45]:
#                     print("gb4 - oldu")
#                     sound = pygame.mixer.Sound(r"C:\Users\suley\Desktop\software\materials\opencv_materials\Piano.ff.G5.mp3")
#                     sound.play()
#                 elif deger == roilerim[46]:
#                     print("g4 - oldu")
#                     sound = pygame.mixer.Sound(r"C:\Users\suley\Desktop\software\materials\opencv_materials\Piano.ff.G5.mp3")
#                     sound.play()
#                 elif deger == roilerim[47]:
#                     print("ab4 - oldu")
#                     sound = pygame.mixer.Sound(r"C:\Users\suley\Desktop\software\materials\opencv_materials\Piano.ff.G5.mp3")
#                     sound.play()
#                 elif deger == roilerim[48]:
#                     print("a4 - oldu")
#                     sound = pygame.mixer.Sound(r"C:\Users\suley\Desktop\software\materials\opencv_materials\Piano.ff.G5.mp3")
#                     sound.play()
#                 elif deger == roilerim[49]:
#                     print("bb4 - oldu")
#                     sound = pygame.mixer.Sound(r"C:\Users\suley\Desktop\software\materials\opencv_materials\Piano.ff.G5.mp3")
#                     sound.play()
#                 elif deger == roilerim[50]:
#                     print("b4 - oldu")
#                     sound = pygame.mixer.Sound(r"C:\Users\suley\Desktop\software\materials\opencv_materials\Piano.ff.G5.mp3")
#                     sound.play()
#                 elif deger == roilerim[51]:
#                     print("c5 - oldu")
#                     sound = pygame.mixer.Sound(r"C:\Users\suley\Desktop\software\materials\opencv_materials\Piano.ff.G5.mp3")
#                     sound.play()
#                 elif deger == roilerim[52]:
#                     print("db5 - oldu")
#                     sound = pygame.mixer.Sound(r"C:\Users\suley\Desktop\software\materials\opencv_materials\Piano.ff.G5.mp3")
#                     sound.play()
#                 elif deger == roilerim[53]:
#                     print("d5 - oldu")
#                     sound = pygame.mixer.Sound(r"C:\Users\suley\Desktop\software\materials\opencv_materials\Piano.ff.G5.mp3")
#                     sound.play()
#                 elif deger == roilerim[54]:
#                     print("eb5 - oldu")
#                     sound = pygame.mixer.Sound(r"C:\Users\suley\Desktop\software\materials\opencv_materials\Piano.ff.G5.mp3")
#                     sound.play()
#                 elif deger == roilerim[55]:
#                     print("e5 - oldu")
#                     sound = pygame.mixer.Sound(r"C:\Users\suley\Desktop\software\materials\opencv_materials\Piano.ff.G5.mp3")
#                     sound.play()
#                 elif deger == roilerim[56]:
#                     print("f5 - oldu")
#                     sound = pygame.mixer.Sound(r"C:\Users\suley\Desktop\software\materials\opencv_materials\Piano.ff.G5.mp3")
#                     sound.play()
#                 elif deger == roilerim[57]:
#                     print("gb5 - oldu")
#                     sound = pygame.mixer.Sound(r"C:\Users\suley\Desktop\software\materials\opencv_materials\Piano.ff.G5.mp3")
#                     sound.play()
#                 elif deger == roilerim[58]:
#                     print("g5 - oldu")
#                     sound = pygame.mixer.Sound(r"C:\Users\suley\Desktop\software\materials\opencv_materials\Piano.ff.G5.mp3")
#                     sound.play()
#                 elif deger == roilerim[59]:
#                     print("ab5 - oldu")
#                     sound = pygame.mixer.Sound(r"C:\Users\suley\Desktop\software\materials\opencv_materials\Piano.ff.G5.mp3")
#                     sound.play()
#                 elif deger == roilerim[60]:
#                     print("a5 - oldu")
#                     sound = pygame.mixer.Sound(r"C:\Users\suley\Desktop\software\materials\opencv_materials\Piano.ff.G5.mp3")
#                     sound.play()
#                 elif deger == roilerim[61]:
#                     print("bb5 - oldu")
#                     sound = pygame.mixer.Sound(r"C:\Users\suley\Desktop\software\materials\opencv_materials\Piano.ff.G5.mp3")
#                     sound.play()
#                 elif deger == roilerim[62]:
#                     print("b5 - oldu")
#                     sound = pygame.mixer.Sound(r"C:\Users\suley\Desktop\software\materials\opencv_materials\Piano.ff.G5.mp3")
#                     sound.play()
#                 elif deger == roilerim[63]:
#                     print("c6 - oldu")
#                     sound = pygame.mixer.Sound(r"C:\Users\suley\Desktop\software\materials\opencv_materials\Piano.ff.G5.mp3")
#                     sound.play()
#                 elif deger == roilerim[64]:
#                     print("db6 - oldu")
#                     sound = pygame.mixer.Sound(r"C:\Users\suley\Desktop\software\materials\opencv_materials\Piano.ff.G5.mp3")
#                     sound.play()
#                 elif deger == roilerim[65]:
#                     print("d6 - oldu")
#                     sound = pygame.mixer.Sound(r"C:\Users\suley\Desktop\software\materials\opencv_materials\Piano.ff.G5.mp3")
#                     sound.play()
#                 elif deger == roilerim[66]:
#                     print("eb6 - oldu")
#                     sound = pygame.mixer.Sound(r"C:\Users\suley\Desktop\software\materials\opencv_materials\Piano.ff.G5.mp3")
#                     sound.play()
#                 elif deger == roilerim[67]:
#                     print("e6 - oldu")
#                     sound = pygame.mixer.Sound(r"C:\Users\suley\Desktop\software\materials\opencv_materials\Piano.ff.G5.mp3")
#                     sound.play()
#                 elif deger == roilerim[68]:
#                     print("f6 - oldu")
#                     sound = pygame.mixer.Sound(r"C:\Users\suley\Desktop\software\materials\opencv_materials\Piano.ff.G5.mp3")
#                     sound.play()
#                 elif deger == roilerim[69]:
#                     print("gb6 - oldu")
#                     sound = pygame.mixer.Sound(r"C:\Users\suley\Desktop\software\materials\opencv_materials\Piano.ff.G5.mp3")
#                     sound.play()
#                 elif deger == roilerim[70]:
#                     print("g6 - oldu")
#                     sound = pygame.mixer.Sound(r"C:\Users\suley\Desktop\software\materials\opencv_materials\Piano.ff.G5.mp3")
#                     sound.play()
#                 elif deger == roilerim[71]:
#                     print("ab6 - oldu")
#                     sound = pygame.mixer.Sound(r"C:\Users\suley\Desktop\software\materials\opencv_materials\Piano.ff.G5.mp3")
#                     sound.play()
#                 elif deger == roilerim[72]:
#                     print("a6 - oldu")
#                     sound = pygame.mixer.Sound(r"C:\Users\suley\Desktop\software\materials\opencv_materials\Piano.ff.G5.mp3")
#                     sound.play()
#                 elif deger == roilerim[73]:
#                     print("bb6 - oldu")
#                     sound = pygame.mixer.Sound(r"C:\Users\suley\Desktop\software\materials\opencv_materials\Piano.ff.G5.mp3")
#                     sound.play()
#                 elif deger == roilerim[74]:
#                     print("b6 - oldu")
#                     sound = pygame.mixer.Sound(r"C:\Users\suley\Desktop\software\materials\opencv_materials\Piano.ff.G5.mp3")
#                     sound.play()
#                 elif deger == roilerim[75]:
#                     print("c7 - oldu")
#                     sound = pygame.mixer.Sound(r"C:\Users\suley\Desktop\software\materials\opencv_materials\Piano.ff.G5.mp3")
#                     sound.play()
#                 elif deger == roilerim[76]:
#                     print("db7 - oldu")
#                     sound = pygame.mixer.Sound(r"C:\Users\suley\Desktop\software\materials\opencv_materials\Piano.ff.G5.mp3")
#                     sound.play()
#                 elif deger == roilerim[77]:
#                     print("d7 - oldu")
#                     sound = pygame.mixer.Sound(r"C:\Users\suley\Desktop\software\materials\opencv_materials\Piano.ff.G5.mp3")
#                     sound.play()
#                 elif deger == roilerim[78]:
#                     print("eb7 - oldu")
#                     sound = pygame.mixer.Sound(r"C:\Users\suley\Desktop\software\materials\opencv_materials\Piano.ff.G5.mp3")
#                     sound.play()
#                 elif deger == roilerim[79]:
#                     print("e7 - oldu")
#                     sound = pygame.mixer.Sound(r"C:\Users\suley\Desktop\software\materials\opencv_materials\Piano.ff.G5.mp3")
#                     sound.play()
#                 elif deger == roilerim[80]:
#                     print("f7 - oldu")
#                     sound = pygame.mixer.Sound(r"C:\Users\suley\Desktop\software\materials\opencv_materials\Piano.ff.G5.mp3")
#                     sound.play()
#                 elif deger == roilerim[81]:
#                     print("gb7 - oldu")
#                     sound = pygame.mixer.Sound(r"C:\Users\suley\Desktop\software\materials\opencv_materials\Piano.ff.G5.mp3")
#                     sound.play()
#                 elif deger == roilerim[82]:
#                     print("g7 - oldu")
#                     sound = pygame.mixer.Sound(r"C:\Users\suley\Desktop\software\materials\opencv_materials\Piano.ff.G5.mp3")
#                     sound.play()
#                 elif deger == roilerim[83]:
#                     print("ab7 - oldu")
#                     sound = pygame.mixer.Sound(r"C:\Users\suley\Desktop\software\materials\opencv_materials\Piano.ff.G5.mp3")
#                     sound.play()
#                 elif deger == roilerim[84]:
#                     print("a7 - oldu")
#                     sound = pygame.mixer.Sound(r"C:\Users\suley\Desktop\software\materials\opencv_materials\Piano.ff.G5.mp3")
#                     sound.play()
#                 elif deger == roilerim[85]:
#                     print("bb7 - oldu")
#                     sound = pygame.mixer.Sound(r"C:\Users\suley\Desktop\software\materials\opencv_materials\Piano.ff.G5.mp3")
#                     sound.play()
#                 elif deger == roilerim[86]:
#                     print("b7 - oldu")
#                     sound = pygame.mixer.Sound(r"C:\Users\suley\Desktop\software\materials\opencv_materials\Piano.ff.G5.mp3")
#                     sound.play()
#                 elif deger == roilerim[87]:
#                     print("c8 - oldu")
#                     sound = pygame.mixer.Sound(r"C:\Users\suley\Desktop\software\materials\opencv_materials\Piano.ff.G5.mp3")
#                     sound.play()
#
#         else:  # eger bottom degeri 20 atlinda ise bu kez sifir verilmesi saglandi bu sayede ses calinmadi
#             b1 = 0
#         return b1  # bu deger tus sayisina donerildi ki bi dahaki seferde 1 gelirse 1 eklense 2 olsun ve ses calmasin
#     except Exception:  # bu sayede icerde parmak beklerse ses calinmaz ancak asagi inince sifir olur ki tekrar gelince
#         b1 = 0  # 1 olsun ve ses calsin. eger disari cikarsa da 0 olsun ki tekrar calmasin ve tekrar girerse 1 olsun
#         return b1  # ve calsin


def bottombul(dst, roilerim, deger, b1, low_hsv, up_hsv):
    try:

        roi = dst[deger[1] - 30: deger[1] + 30, deger[0] - 20: deger[0] + 20]
        hsv = cv2.cvtColor(roi, cv2.COLOR_BGR2HSV)

        # hazir dosya ise renkler boyle kalsin
        lower_skin = np.array([0, 90, 130], dtype=np.uint8)
        upper_skin = np.array([20, 255, 255], dtype=np.uint8)
        mask = cv2.inRange(hsv, lower_skin, upper_skin)

        # her defasinda renk kodlari alinirsa bunu al
        # mask = cv2.inRange(hsv, low_hsv, up_hsv)

        kernel = np.ones((3, 3), np.uint8)
        mask = cv2.dilate(mask, kernel, iterations=4)
        mask = cv2.GaussianBlur(mask, (5, 5), 100)
        contours, _ = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

        cv2.drawContours(roi, contours, -1, (0, 255, 0), 2)

        areas = [cv2.contourArea(c) for c in contours]
        min_index = np.argmax(areas)
        cnt = contours[min_index]
        bottommost = tuple(cnt[cnt[:, :, 1].argmax()][0])
        cv2.circle(roi, bottommost, 5, (0, 0, 255), -1)

        if bottommost[1] > 20:
            b1 += 1

            if b1 == 1:
                if deger == roilerim[0]:
                    print("1 - bb4.mp3 - oldu")
                    sound = pygame.mixer.Sound(r"C:\Users\suley\Desktop\software\materials\opencv_materials\chopinnotes\1 - bb4.mp3")
                    sound.play()
                elif deger == roilerim[1]:
                    print("2 - b4.mp3 - oldu")
                    sound = pygame.mixer.Sound(r"C:\Users\suley\Desktop\software\materials\opencv_materials\chopinnotes\2 - b4.mp3")
                    sound.play()
                elif deger == roilerim[2]:
                    print("3 - c5.mp3 - oldu")
                    sound = pygame.mixer.Sound(r"C:\Users\suley\Desktop\software\materials\opencv_materials\chopinnotes\3 - c5.mp3")
                    sound.play()
                elif deger == roilerim[3]:
                    print("4 - db5.mp3 - oldu")
                    sound = pygame.mixer.Sound(r"C:\Users\suley\Desktop\software\materials\opencv_materials\chopinnotes\4 - db5.mp3")
                    sound.play()
                elif deger == roilerim[4]:
                    print("5 - d5.mp3 - oldu")
                    sound = pygame.mixer.Sound(r"C:\Users\suley\Desktop\software\materials\opencv_materials\chopinnotes\5 - d5.mp3")
                    sound.play()
                elif deger == roilerim[5]:
                    print("6 - eb5.mp3 - oldu")
                    sound = pygame.mixer.Sound(r"C:\Users\suley\Desktop\software\materials\opencv_materials\chopinnotes\6 - eb5.mp3")
                    sound.play()
                elif deger == roilerim[6]:
                    print("7 - f5.mp3 - oldu")
                    sound = pygame.mixer.Sound(r"C:\Users\suley\Desktop\software\materials\opencv_materials\chopinnotes\7 - f5.mp3")
                    sound.play()
                elif deger == roilerim[7]:
                    print("8 - g5.mp3 - oldu")
                    sound = pygame.mixer.Sound(r"C:\Users\suley\Desktop\software\materials\opencv_materials\chopinnotes\8 - g5.mp3")
                    sound.play()
                elif deger == roilerim[8]:
                    print("9 - ab5.mp3 - oldu")
                    sound = pygame.mixer.Sound(r"C:\Users\suley\Desktop\software\materials\opencv_materials\chopinnotes\9 - ab5.mp3")
                    sound.play()
                elif deger == roilerim[9]:
                    print("10 - bb5.mp3 - oldu")
                    sound = pygame.mixer.Sound(r"C:\Users\suley\Desktop\software\materials\opencv_materials\chopinnotes\10 - bb5.mp3")
                    sound.play()
                elif deger == roilerim[10]:
                    print("11 - c6.mp3 - oldu")
                    sound = pygame.mixer.Sound(r"C:\Users\suley\Desktop\software\materials\opencv_materials\chopinnotes\11 - c6.mp3")
                    sound.play()
                elif deger == roilerim[11]:
                    print("12 - d6.mp3 - oldu")
                    sound = pygame.mixer.Sound(r"C:\Users\suley\Desktop\software\materials\opencv_materials\chopinnotes\12 - d6.mp3")
                    sound.play()

        else:
            b1 = 0
        return b1
    except Exception:
        b1 = 0
        return b1
