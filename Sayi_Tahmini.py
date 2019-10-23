import time
import random

print('Sayi tahmini oyununa hosgeldiniz... Lutfen 1 ile 100 arasinda bir sayi seciniz...')
sayi = random.randint(1,100)
tahmin_hakki = 5

while True:
    tahmin = int(input("Tahmininiz : "))

    if tahmin == sayi :
        print('Sayi sorgulaniyor...')
        time.sleep(1)
        print("Tebrikler Dogru Tahmin !!!")
        break

    elif tahmin > sayi :
        print("Sayi sorgulaniyor...")
        time.sleep(1)
        tahmin_hakki -=1
        print('Daha kucuk bir sayi giriniz ')
        print("Kalan tahmin hakki :",tahmin_hakki)

    else:
        print('Sayi sorgulaniyor...')
        time.sleep(1)
        tahmin_hakki -= 1
        print('Daha buyuk bir sayi giriniz ')
        print("Kalan tahmin hakki :", tahmin_hakki)

    if tahmin_hakki == 0 :
        print("Tahmin hakkiniz bitmistir")
        print("Bilgisayarin tuttugu sayi : ",sayi)
        break