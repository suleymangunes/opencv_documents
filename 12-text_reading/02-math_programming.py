import cv2  # opencv kutuphanesi ice aktarildi
from PIL import Image  # grafik isleyen kutuphane ice aktarildi
import pytesseract  # resimdeki karakterleri algilayan modul ice aktarildi

cap = cv2.VideoCapture(r"C:\Users\suley\Desktop\software\materials\opencv_materials\toplama_video.mp4")
# video opencv de islenmek uzere ice aktarildi

file_name = r"C:\Users\suley\Desktop\software\materials\opencv_materials\toplama_fotolar\video.avi"
codec = cv2.VideoWriter_fourcc("W", "M", "V", "2")
frame_rate = 30
resolution = (840, 510)
video_save = cv2.VideoWriter(file_name, codec, frame_rate, resolution)
# videonun uzerine uygulanan methodlardan sonra tekrar kaydedilmesi icin ozellikler ve fonksiyon tanimlandi

while True:
    ret, frame = cap.read()  # kare okundu ve kare degeri frame'e atandi, ret ise degerin olup olmadigi ile ingilenir
    if ret == 0:  # eger deger dondurmezse yani kare bittiyse donguden cikilmasi saglandi
        break
    row, col, hc = frame.shape  # karenin yuksekligi genisligi ve renklendirilme ozelligi degiskenlere atandi

    cv2.imwrite(r"C:\Users\suley\Desktop\software\materials\opencv_materials\toplama_fotolar\write_img.jpg", frame)
    # grafik methodu ile calismasi icin frame kaydedildi

    img = Image.open(r"C:\Users\suley\Desktop\software\materials\opencv_materials\toplama_fotolar\write_img.jpg")
    # kaydedilen resim pil kutuphanesi araciligiyla acildi

    text = pytesseract.image_to_boxes(img, lang="eng")  # tesseract ile karedeki yazi okundu
    text = text.split("\n")  # yazi kutu seklinde ciktigi icin satirlar birbirinden ayrildi

    try:  # eger listede bos deger var ise silinmesi saglandi yok ise devam edildi
        bos_index = text.index("")
        text.pop(bos_index)
    except Exception:
        pass

    x_index_list = []  # resimdeki karakterlerin koordinatlari bulunmasi icin x koordinat degerleri liste icine alindi
    liste = []  # resimdeki karakterler, kutu listesi icerisinde olan ilk degerler oldugundan bu degerler listeye
    # tanimlanmak uzere bos liste tanimlandi

    for i in text:  # kutudaki string degerler bosluk ile ayrilarak gerekli listelere eklenmesi saglandi
        i = i.split(" ")
        liste.append(i[0])
        x_index_list.append((i[1], i[2]))
        (x, y, w, h) = int(i[1]), int(i[2]), int(i[3]), int(i[4])  # her kararkteri saracak dortgen icin koordinatlar
        cv2.rectangle(frame, (x, row - h), (w, row - y), (0, 255, 0), 2)  # belirlendi ve dortgen cizildi

    try:  # framelerde liste sayi veya eksik deger bulunurdugunda hata vermeyip bi sonrkai listede tekrar denenmesi
          # uzerinde try except bloguna alindi
        basamak = []  # iki basamaklari sayilari listede birlestirmek icin bos liste tanimlandi
        p = 0
        sayi = 0  # iki basamakli sayinin atanacagi degisken tanimlandi
        for i in range(len(liste) * 5):    # GELİSTİRİLMESİ LAZIM
        # sirayla listede donup iki basamakli sayilari belirlenip duzenlenen dongu tanimlandi
            try:  # eger listede integere cevrilecek deger varsa yani deger sayi ise basamak listesine eklendi
                liste[p] = int(liste[p])
                basamak.append((p, liste[p]))

            except:  # aksi duruma basamaktaki degerler ile yeni sayi olusturuldu tabi degerler iceriyosa!
                m = 0
                if len(basamak) >= 2:  # degerler iceriyosa

                    for i in range(len(basamak)):  # degerler kadar donen dongu ile
                        sayi = str(sayi) + str(basamak[i][1])  # yeni sayi belirlendi

                    for i in range(len(basamak)):  # asil listede basamakta kullanilan degerlerin indisleri silindi
                        liste.pop(basamak[0][0])  # bu sayede degerler silinip tek deger eklenmenin onu acildi

                    liste.insert(basamak[0][0], int(sayi[1:]))  # asil listeye yeni sayi degeri eklendi
                    basamak.clear()  # basamak temizlendi
                    sayi = 0  # sayi degeri tekrar sifir olarak ayarlandi
                    p = 0  # p degeri tekrar sifir olarak ayarlandi ve listede baska 2 veya daha yuksek basamakli
                    # degerler tekrar listeye dogru sekilde eklenmis oldu
                    continue

                elif len(basamak) < 2:  # eger tek basamakli ise basmaak listesinin silinip tekrar aranmasi saglandi
                    basamak.clear()

            p = p + 1

        soa = int(x_index_list[0][0]), row - int(x_index_list[0][1])  # listedeki ilk ikimci ve son degerlerin sol alt
        soa2 = int(x_index_list[1][0]), row - int(x_index_list[1][1])   # koordinat degerleri bulundu
        soason = int(x_index_list[-2][0]), row - int(x_index_list[-2][1])

        sayilar_arasi_uzaklik = soa2[0] - soa[0]  # sayilar arasi uzaklik belirlendi bu sayede sonuc kisminin yazilmasi
        yeni_bolge = (soason[0] + int(sayilar_arasi_uzaklik * 2.2), soason[1])  # tahmini yer olusturulmus oldu

        esit_index = liste.index("=")  # listede esittir isaretinden onceki kismin secilmesi saglandi
        liste = liste[:esit_index]
        liste_cb = []  # carpma ve bolmee degerlerinin indislerini ve operatorlerini tutacak liste tanimlandi
        liste_ct = []  # cikarma ve toplama degerlerinin indislerini ve operatorlerini tutacak liste tanimlandi


        def listele():  # listede donup her defasinda carpma ve bolme degerlerinin operator ve indislerini tutan
            z = 0  # fonksiyon tanimlandi
            global liste_cb  # liste degerlerine global ozellik kazandirildi bu sayede fonksiyon disinda da aktif olacak
            global liste
            for i in liste:
                if i == "*" or i == "/":
                    if i == "*":
                        liste_cb.append(("*", z))
                    elif i == "/":
                        liste_cb.append(("/", z))
                z = z + 1
            return liste_cb


        def listele2():  # listede donup her defasinda cikarma ve toplama degerlerinin operator ve indislerini tutan
            k = 0  # fonksiyon tanimlandi
            global liste_ct  # liste degerlerine global ozellik kazandirildi bu sayede fonksiyon disinda da aktif olacak
            global liste
            for i in liste:
                if i == "+" or i == "-":
                    if i == "+":
                        liste_ct.append(("+", k))
                    elif i == "-":
                        liste_ct.append(("-", k))
                k = k + 1
            return liste_ct


        listele()  # islem onceliginden dolayi once carpma ve bolme islemlerini yapmasi icin once bu fonksiyon cagrildi

        if liste_cb is not None:  # eger liste bos degilse yani islemimizde carpma bolme varsa
            for r in range(len(liste_cb)):  # listedeki deger kadar donen dongu ile
                i = liste_cb[0]  # listenin ilk degeri secilmesi saglandi
                if i[0] == "*":  # ve ilk degerin tuple listenin ilk degeri carpim operatoru ise
                    islem1 = int(liste[i[1] - 1]) * int(liste[i[1] + 1])  # kendinden oncek ice sonraki degerlerin
                    # carpilmasi saglandi
                    liste[i[1] - 1] = islem1  # kendinden onceki degere sonuc aktarildi ve artik fazlalik olan
                    liste.pop(i[1] + 1)  # carpim degeri ve sonraki deger silindi
                    liste.pop(i[1])
                    liste_cb.pop(0)  # liste silindi cunku artik ayni indis degerleri yanlis sonuc uretecekti
                    liste_cb.clear()  # bu yuzden listele fonksiyonu tekrar cagrildi ve tekrar icerdeki diger
                    listele()  # opeartorleri bulup yeni indis degerleri verdi

                elif i[0] == "/":  # eger ilk deger bolum ise carpimda uygulanan islemlerin bolum icin olanlari uyguladi
                    islem2 = int(liste[i[1] - 1]) / int(liste[int(i[1]) + 1])
                    liste[i[1] - 1] = islem2
                    liste.pop(i[1] + 1)
                    liste.pop(i[1])
                    liste_cb.pop(0)
                    liste_cb.clear()
                    listele()

        listele2()  # daha sonra toplama ve cikarma islemleri yapilmak uzere ikindi listele fonksiyonu tanimlandi

        if liste_ct is not None:  # carpim icin uygulanan methodun toplama ve cikarma icin olani bu kisimda uygulandi
            for q in range(len(liste_ct)):
                i = liste_ct[0]
                if i[0] == "+":
                    islem3 = int(liste[i[1] - 1]) + int(liste[i[1] + 1])
                    liste[i[1] - 1] = islem3
                    liste.pop(i[1] + 1)
                    liste.pop(i[1])
                    liste_ct.pop(0)
                    liste_ct.clear()
                    listele2()

                elif i[0] == "-":
                    islem4 = int(liste[i[1] - 1]) - int(liste[int(i[1]) + 1])
                    liste[i[1] - 1] = islem4
                    liste.pop(i[1] + 1)
                    liste.pop(i[1])
                    liste_ct.pop(0)
                    liste_ct.clear()
                    listele2()
        # listede kalan son deger sonuc degeri olarak kalmis oldu yani sonuc bulundu

        if sayilar_arasi_uzaklik < 10:
            font_buyukluk = 1
        elif sayilar_arasi_uzaklik < 35 and sayilar_arasi_uzaklik > 10:
            font_buyukluk = 2
        elif sayilar_arasi_uzaklik < 55 and sayilar_arasi_uzaklik > 35:
            font_buyukluk = 3
        elif sayilar_arasi_uzaklik < 85 and sayilar_arasi_uzaklik > 55:
            font_buyukluk = 4
        elif sayilar_arasi_uzaklik > 85:
            font_buyukluk = 5
        else:
            font_buyukluk = 6
        # sayilar arasindaki uzakliga gore font buyuklugu ayarlandi

        cv2.putText(frame, f"{liste[0]}", yeni_bolge, cv2.FONT_HERSHEY_SIMPLEX, font_buyukluk, (0, 0, 255), 5)
        # sonuc degeri ekran olmasi gerekn koordinatta ve buyuklukte yazilmasi saglandi
    except:  # eger kodlar hata verirse de excep blogu kodu durdurmadan bulamadi yazisini gonderdi
        print("Sonucun bulunmasi zaman alabilir, lütfen bekleyin...")

    cv2.imshow("frame", frame)  # kare ekranda gosterildi
    video_save.write(frame)  # gosterilen kare de video olarak kaydedildi

    if cv2.waitKey(1) & 0xFF == ord("q"):  # eger q tusuna basilirsa cikilmasi saglandi
        break

cap.release()  # video serbest birakildi
cv2.destroyAllWindows()  # tek tusa basilirsa acik tum pencerelerin kapatilmasi saglandi
