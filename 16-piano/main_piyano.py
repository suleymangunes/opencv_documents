import cv2
import ultis
from multiprocessing.pool import ThreadPool

# 1 - img resize ile daha ayrintili daha fazla kareli daha iyi sonuc veren yapi olusuturulabilir
# 2 - on kamera ile islem yapilip akan notalar yapilabilir
# 3 - el ile belirli el isareti yapilip el isareti bulunana dek renk kodlarini ayirip uygun renk kodu algilanabilir
# bu sayede insanlar ayarlamak zorunda kalmaz
# ayni islem ile midi mix melodika vs yapılabilir
# 4 - roiler kalip olarak yerlestirilmeli, pencere buyuklugunu bolerek bu saglanabilir
# 5 - 88 piyano tusu verilir sadece beyazlar bunlar arasinda gecis yapilabilir
# 6 - ya da istenirse belirli sarkilar icin belirli notalar eklenebilir
# 7 - klavye opencv dosyalarini incele bununla siyah tuslari ayarlamaya calisabilirsin
# 8 - main dosyasindaki t degerleri icin daha kisa kod dusunulmeli
# 9 - thread fonksiyonlarini da daha kisa yapmaya calis


# hsv renk kodlari bulunmus oldu
low_hsv, up_hsv = ultis.hsvbul()

# perspektif yapilacak matrix degeri bulundu warppers ile persi alinir
matrix = ultis.pers_noktalari()

# notalari saklayacak roi noktalari bulundu
roilerim = ultis.roi_noktalari(matrix)
print("roilerim", roilerim)

cap = cv2.VideoCapture(1, cv2.CAP_DSHOW)

t1 = 0  # tuslarar sifir degeri baslangicta verilmeli ki belirlene fonkisyona uysun
t2 = 0
t3 = 0
t4 = 0
t5 = 0
t6 = 0
t7 = 0
t8 = 0
t9 = 0
t10 = 0
t11 = 0
t12 = 0
t13 = 0
t14 = 0
t15 = 0
t16 = 0
t17 = 0
t18 = 0
t19 = 0
t20 = 0
t21 = 0
t22 = 0
t23 = 0
t24 = 0
t25 = 0
t26 = 0
t27 = 0
t28 = 0
t29 = 0
t30 = 0
t31 = 0
t32 = 0
t33 = 0
t34 = 0
t35 = 0
t36 = 0
t37 = 0
t38 = 0
t39 = 0
t40 = 0
t41 = 0
t42 = 0
t43 = 0
t44 = 0
t45 = 0
t46 = 0
t47 = 0
t48 = 0
t49 = 0
t50 = 0
t51 = 0
t52 = 0
t53 = 0
t54 = 0
t55 = 0
t56 = 0
t57 = 0
t58 = 0
t59 = 0
t60 = 0
t61 = 0
t62 = 0
t63 = 0
t64 = 0
t65 = 0
t66 = 0
t67 = 0
t68 = 0
t69 = 0
t70 = 0
t71 = 0
t72 = 0
t73 = 0
t74 = 0
t75 = 0
t76 = 0
t77 = 0
t78 = 0
t79 = 0
t80 = 0
t81 = 0
t82 = 0
t83 = 0
t84 = 0
t85 = 0
t86 = 0
t87 = 0
t88 = 0

while True:
    ret, frame = cap.read()
    if ret == 0:
        break
    frame = cv2.resize(frame, (960, 540))
    frame = cv2.flip(frame, 1)
    # disardan alinen deger ile dst'ye pers uygulandi
    dst = cv2.warpPerspective(frame, matrix, (960, 540))
    # pers yapilmis deger uzerinde roileri gosteren dortgenler cizildi
    ultis.roi_dortgenleri(roilerim, dst)

    # thread ile tum sonfkiyonalarin eszamanli calimasi saglandi
    t1 = ThreadPool(processes=1).apply_async(ultis.bottombul, (dst, roilerim, roilerim[0], t1, low_hsv, up_hsv))
    t1 = t1.get()
    t2 = ThreadPool(processes=1).apply_async(ultis.bottombul, (dst, roilerim, roilerim[1], t2, low_hsv, up_hsv))
    t2 = t2.get()
    t3 = ThreadPool(processes=1).apply_async(ultis.bottombul, (dst, roilerim, roilerim[2], t3, low_hsv, up_hsv))
    t3 = t3.get()
    t4 = ThreadPool(processes=1).apply_async(ultis.bottombul, (dst, roilerim, roilerim[3], t4, low_hsv, up_hsv))
    t4 = t4.get()
    t5 = ThreadPool(processes=1).apply_async(ultis.bottombul, (dst, roilerim, roilerim[4], t5, low_hsv, up_hsv))
    t5 = t5.get()
    t6 = ThreadPool(processes=1).apply_async(ultis.bottombul, (dst, roilerim, roilerim[5], t6, low_hsv, up_hsv))
    t6 = t6.get()
    t7 = ThreadPool(processes=1).apply_async(ultis.bottombul, (dst, roilerim, roilerim[6], t7, low_hsv, up_hsv))
    t7 = t7.get()
    t8 = ThreadPool(processes=1).apply_async(ultis.bottombul, (dst, roilerim, roilerim[7], t8, low_hsv, up_hsv))
    t8 = t8.get()
    t9 = ThreadPool(processes=1).apply_async(ultis.bottombul, (dst, roilerim, roilerim[8], t9, low_hsv, up_hsv))
    t9 = t9.get()
    t10 = ThreadPool(processes=1).apply_async(ultis.bottombul, (dst, roilerim, roilerim[9], t10, low_hsv, up_hsv))
    t10 = t10.get()
    t11 = ThreadPool(processes=1).apply_async(ultis.bottombul, (dst, roilerim, roilerim[10], t11, low_hsv, up_hsv))
    t11 = t11.get()
    t12 = ThreadPool(processes=1).apply_async(ultis.bottombul, (dst, roilerim, roilerim[11], t12, low_hsv, up_hsv))
    t12 = t12.get()
    # t13 = ThreadPool(processes=1).apply_async(ultis.bottombul, (dst, roilerim, roilerim[12], t13, low_hsv, up_hsv))
    # t13 = t13.get()
    # t14 = ThreadPool(processes=1).apply_async(ultis.bottombul, (dst, roilerim, roilerim[13], t14, low_hsv, up_hsv))
    # t14 = t14.get()
    # t15 = ThreadPool(processes=1).apply_async(ultis.bottombul, (dst, roilerim, roilerim[14], t15, low_hsv, up_hsv))
    # t15 = t15.get()
    # t16 = ThreadPool(processes=1).apply_async(ultis.bottombul, (dst, roilerim, roilerim[15], t16, low_hsv, up_hsv))
    # t16 = t16.get()
    # t17 = ThreadPool(processes=1).apply_async(ultis.bottombul, (dst, roilerim, roilerim[16], t17, low_hsv, up_hsv))
    # t17 = t17.get()
    # t18 = ThreadPool(processes=1).apply_async(ultis.bottombul, (dst, roilerim, roilerim[17], t18, low_hsv, up_hsv))
    # t18 = t18.get()
    # t19 = ThreadPool(processes=1).apply_async(ultis.bottombul, (dst, roilerim, roilerim[18], t19, low_hsv, up_hsv))
    # t19 = t19.get()
    # t20 = ThreadPool(processes=1).apply_async(ultis.bottombul, (dst, roilerim, roilerim[19], t20, low_hsv, up_hsv))
    # t20 = t20.get()
    # t21 = ThreadPool(processes=1).apply_async(ultis.bottombul, (dst, roilerim, roilerim[20], t21, low_hsv, up_hsv))
    # t21 = t21.get()
    # t22 = ThreadPool(processes=1).apply_async(ultis.bottombul, (dst, roilerim, roilerim[21], t22, low_hsv, up_hsv))
    # t22 = t22.get()
    # t23 = ThreadPool(processes=1).apply_async(ultis.bottombul, (dst, roilerim, roilerim[22], t23, low_hsv, up_hsv))
    # t23 = t23.get()
    # t24 = ThreadPool(processes=1).apply_async(ultis.bottombul, (dst, roilerim, roilerim[23], t24, low_hsv, up_hsv))
    # t24 = t24.get()
    # t25 = ThreadPool(processes=1).apply_async(ultis.bottombul, (dst, roilerim, roilerim[24], t25, low_hsv, up_hsv))
    # t25 = t25.get()
    # t26 = ThreadPool(processes=1).apply_async(ultis.bottombul, (dst, roilerim, roilerim[25], t26, low_hsv, up_hsv))
    # t26 = t26.get()
    # t27 = ThreadPool(processes=1).apply_async(ultis.bottombul, (dst, roilerim, roilerim[26], t27, low_hsv, up_hsv))
    # t27 = t27.get()
    # t28 = ThreadPool(processes=1).apply_async(ultis.bottombul, (dst, roilerim, roilerim[27], t28, low_hsv, up_hsv))
    # t28 = t28.get()
    # t29 = ThreadPool(processes=1).apply_async(ultis.bottombul, (dst, roilerim, roilerim[28], t29, low_hsv, up_hsv))
    # t29 = t29.get()
    # t30 = ThreadPool(processes=1).apply_async(ultis.bottombul, (dst, roilerim, roilerim[29], t30, low_hsv, up_hsv))
    # t30 = t30.get()
    # t31 = ThreadPool(processes=1).apply_async(ultis.bottombul, (dst, roilerim, roilerim[30], t31, low_hsv, up_hsv))
    # t31 = t31.get()
    # t32 = ThreadPool(processes=1).apply_async(ultis.bottombul, (dst, roilerim, roilerim[31], t32, low_hsv, up_hsv))
    # t32 = t32.get()
    # t33 = ThreadPool(processes=1).apply_async(ultis.bottombul, (dst, roilerim, roilerim[32], t33, low_hsv, up_hsv))
    # t33 = t33.get()
    # t34 = ThreadPool(processes=1).apply_async(ultis.bottombul, (dst, roilerim, roilerim[33], t34, low_hsv, up_hsv))
    # t34 = t34.get()
    # t35 = ThreadPool(processes=1).apply_async(ultis.bottombul, (dst, roilerim, roilerim[34], t35, low_hsv, up_hsv))
    # t35 = t35.get()
    # t36 = ThreadPool(processes=1).apply_async(ultis.bottombul, (dst, roilerim, roilerim[35], t36, low_hsv, up_hsv))
    # t36 = t36.get()
    # t37 = ThreadPool(processes=1).apply_async(ultis.bottombul, (dst, roilerim, roilerim[36], t37, low_hsv, up_hsv))
    # t37 = t37.get()
    # t38 = ThreadPool(processes=1).apply_async(ultis.bottombul, (dst, roilerim, roilerim[37], t38, low_hsv, up_hsv))
    # t38 = t38.get()
    # t39 = ThreadPool(processes=1).apply_async(ultis.bottombul, (dst, roilerim, roilerim[38], t39, low_hsv, up_hsv))
    # t39 = t39.get()
    # t40 = ThreadPool(processes=1).apply_async(ultis.bottombul, (dst, roilerim, roilerim[39], t40, low_hsv, up_hsv))
    # t40 = t40.get()
    # t41 = ThreadPool(processes=1).apply_async(ultis.bottombul, (dst, roilerim, roilerim[40], t41, low_hsv, up_hsv))
    # t41 = t41.get()
    # t42 = ThreadPool(processes=1).apply_async(ultis.bottombul, (dst, roilerim, roilerim[41], t42, low_hsv, up_hsv))
    # t42 = t42.get()
    # t43 = ThreadPool(processes=1).apply_async(ultis.bottombul, (dst, roilerim, roilerim[42], t43, low_hsv, up_hsv))
    # t43 = t43.get()
    # t44 = ThreadPool(processes=1).apply_async(ultis.bottombul, (dst, roilerim, roilerim[43], t44, low_hsv, up_hsv))
    # t44 = t44.get()
    # t45 = ThreadPool(processes=1).apply_async(ultis.bottombul, (dst, roilerim, roilerim[44], t45, low_hsv, up_hsv))
    # t45 = t45.get()
    # t46 = ThreadPool(processes=1).apply_async(ultis.bottombul, (dst, roilerim, roilerim[45], t46, low_hsv, up_hsv))
    # t46 = t46.get()
    # t47 = ThreadPool(processes=1).apply_async(ultis.bottombul, (dst, roilerim, roilerim[46], t47, low_hsv, up_hsv))
    # t47 = t47.get()
    # t48 = ThreadPool(processes=1).apply_async(ultis.bottombul, (dst, roilerim, roilerim[47], t48, low_hsv, up_hsv))
    # t48 = t48.get()
    # t49 = ThreadPool(processes=1).apply_async(ultis.bottombul, (dst, roilerim, roilerim[48], t49, low_hsv, up_hsv))
    # t49 = t49.get()
    # t50 = ThreadPool(processes=1).apply_async(ultis.bottombul, (dst, roilerim, roilerim[49], t50, low_hsv, up_hsv))
    # t50 = t50.get()
    # t51 = ThreadPool(processes=1).apply_async(ultis.bottombul, (dst, roilerim, roilerim[50], t51, low_hsv, up_hsv))
    # t51 = t51.get()
    # t52 = ThreadPool(processes=1).apply_async(ultis.bottombul, (dst, roilerim, roilerim[51], t52, low_hsv, up_hsv))
    # t52 = t52.get()
    # t53 = ThreadPool(processes=1).apply_async(ultis.bottombul, (dst, roilerim, roilerim[52], t53, low_hsv, up_hsv))
    # t53 = t53.get()
    # t54 = ThreadPool(processes=1).apply_async(ultis.bottombul, (dst, roilerim, roilerim[53], t54, low_hsv, up_hsv))
    # t54 = t54.get()
    # t55 = ThreadPool(processes=1).apply_async(ultis.bottombul, (dst, roilerim, roilerim[54], t55, low_hsv, up_hsv))
    # t55 = t55.get()
    # t56 = ThreadPool(processes=1).apply_async(ultis.bottombul, (dst, roilerim, roilerim[55], t56, low_hsv, up_hsv))
    # t56 = t56.get()
    # t57 = ThreadPool(processes=1).apply_async(ultis.bottombul, (dst, roilerim, roilerim[56], t57, low_hsv, up_hsv))
    # t57 = t57.get()
    # t58 = ThreadPool(processes=1).apply_async(ultis.bottombul, (dst, roilerim, roilerim[57], t58, low_hsv, up_hsv))
    # t58 = t58.get()
    # t59 = ThreadPool(processes=1).apply_async(ultis.bottombul, (dst, roilerim, roilerim[58], t59, low_hsv, up_hsv))
    # t59 = t59.get()
    # t60 = ThreadPool(processes=1).apply_async(ultis.bottombul, (dst, roilerim, roilerim[59], t60, low_hsv, up_hsv))
    # t60 = t60.get()
    # t61 = ThreadPool(processes=1).apply_async(ultis.bottombul, (dst, roilerim, roilerim[60], t61, low_hsv, up_hsv))
    # t61 = t61.get()
    # t62 = ThreadPool(processes=1).apply_async(ultis.bottombul, (dst, roilerim, roilerim[61], t62, low_hsv, up_hsv))
    # t62 = t62.get()
    # t63 = ThreadPool(processes=1).apply_async(ultis.bottombul, (dst, roilerim, roilerim[62], t63, low_hsv, up_hsv))
    # t63 = t63.get()
    # t64 = ThreadPool(processes=1).apply_async(ultis.bottombul, (dst, roilerim, roilerim[63], t64, low_hsv, up_hsv))
    # t64 = t64.get()
    # t65 = ThreadPool(processes=1).apply_async(ultis.bottombul, (dst, roilerim, roilerim[64], t65, low_hsv, up_hsv))
    # t65 = t65.get()
    # t66 = ThreadPool(processes=1).apply_async(ultis.bottombul, (dst, roilerim, roilerim[65], t66, low_hsv, up_hsv))
    # t66 = t66.get()
    # t67 = ThreadPool(processes=1).apply_async(ultis.bottombul, (dst, roilerim, roilerim[66], t67, low_hsv, up_hsv))
    # t67 = t67.get()
    # t68 = ThreadPool(processes=1).apply_async(ultis.bottombul, (dst, roilerim, roilerim[67], t68, low_hsv, up_hsv))
    # t68 = t68.get()
    # t69 = ThreadPool(processes=1).apply_async(ultis.bottombul, (dst, roilerim, roilerim[68], t69, low_hsv, up_hsv))
    # t69 = t69.get()
    # t70 = ThreadPool(processes=1).apply_async(ultis.bottombul, (dst, roilerim, roilerim[69], t70, low_hsv, up_hsv))
    # t70 = t70.get()
    # t71 = ThreadPool(processes=1).apply_async(ultis.bottombul, (dst, roilerim, roilerim[70], t71, low_hsv, up_hsv))
    # t71 = t71.get()
    # t72 = ThreadPool(processes=1).apply_async(ultis.bottombul, (dst, roilerim, roilerim[71], t72, low_hsv, up_hsv))
    # t72 = t72.get()
    # t73 = ThreadPool(processes=1).apply_async(ultis.bottombul, (dst, roilerim, roilerim[72], t73, low_hsv, up_hsv))
    # t73 = t73.get()
    # t74 = ThreadPool(processes=1).apply_async(ultis.bottombul, (dst, roilerim, roilerim[73], t74, low_hsv, up_hsv))
    # t74 = t74.get()
    # t75 = ThreadPool(processes=1).apply_async(ultis.bottombul, (dst, roilerim, roilerim[74], t75, low_hsv, up_hsv))
    # t75 = t75.get()
    # t76 = ThreadPool(processes=1).apply_async(ultis.bottombul, (dst, roilerim, roilerim[75], t76, low_hsv, up_hsv))
    # t76 = t76.get()
    # t77 = ThreadPool(processes=1).apply_async(ultis.bottombul, (dst, roilerim, roilerim[76], t77, low_hsv, up_hsv))
    # t77 = t77.get()
    # t78 = ThreadPool(processes=1).apply_async(ultis.bottombul, (dst, roilerim, roilerim[77], t78, low_hsv, up_hsv))
    # t78 = t78.get()
    # t79 = ThreadPool(processes=1).apply_async(ultis.bottombul, (dst, roilerim, roilerim[78], t79, low_hsv, up_hsv))
    # t79 = t79.get()
    # t80 = ThreadPool(processes=1).apply_async(ultis.bottombul, (dst, roilerim, roilerim[79], t80, low_hsv, up_hsv))
    # t80 = t80.get()
    # t81 = ThreadPool(processes=1).apply_async(ultis.bottombul, (dst, roilerim, roilerim[80], t81, low_hsv, up_hsv))
    # t81 = t81.get()
    # t82 = ThreadPool(processes=1).apply_async(ultis.bottombul, (dst, roilerim, roilerim[81], t82, low_hsv, up_hsv))
    # t82 = t82.get()
    # t83 = ThreadPool(processes=1).apply_async(ultis.bottombul, (dst, roilerim, roilerim[82], t83, low_hsv, up_hsv))
    # t83 = t83.get()
    # t84 = ThreadPool(processes=1).apply_async(ultis.bottombul, (dst, roilerim, roilerim[83], t84, low_hsv, up_hsv))
    # t84 = t84.get()
    # t85 = ThreadPool(processes=1).apply_async(ultis.bottombul, (dst, roilerim, roilerim[84], t85, low_hsv, up_hsv))
    # t85 = t85.get()
    # t86 = ThreadPool(processes=1).apply_async(ultis.bottombul, (dst, roilerim, roilerim[85], t86, low_hsv, up_hsv))
    # t86 = t86.get()
    # t87 = ThreadPool(processes=1).apply_async(ultis.bottombul, (dst, roilerim, roilerim[86], t87, low_hsv, up_hsv))
    # t87 = t87.get()
    # t88 = ThreadPool(processes=1).apply_async(ultis.bottombul, (dst, roilerim, roilerim[87], t88, low_hsv, up_hsv))
    # t88 = t88.get()

    cv2.imshow("frame", frame)
    cv2.imshow("dst", dst)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()
