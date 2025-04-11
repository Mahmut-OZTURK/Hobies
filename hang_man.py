

import random
kelimeler = ['metallica','araba', 'siber','defense','gomulu']
kelime = random.choice(kelimeler)
new_dizi = len(kelime) * ["_"]
ad = input("hoş geldiniz isminiz: ")
print(f"başarılar {ad} , sana özel kelime geliyor")
ex_letters = set()
#print(type(harf))
can = 10
tahmin_can = 3
while '_' in new_dizi:
    giris = input("bir harf girin ya da kelime tahmin etmek için 'tahmin' yazın ").lower()

    
    if giris == "tahmin":
        tahmin = input("kelimeyi tahmin edin ")
       
        if tahmin == kelime:
            print(f"doğru bildiniz kelime {tahmin}")
            break
       
        else:
            tahmin_can -= 1
            print(f"{tahmin_can} kadar tahmin etme hakkınız kaldı")
            if tahmin_can == 0:
                print(f"bilemediniz kelime : {kelime}'ydi")
                break
    
    else:
        harf = giris
        if len(harf) != 1:
            print("SADECE HARF GİRİN")
            print("\n")
        else :
            if harf in ex_letters:
                print("bu harf kullanılmış başka harf seç")
                continue
            else:  
                if harf in kelime:
                    for(index, karakter) in enumerate(kelime):
               
                        if karakter == harf:
                            new_dizi[index] = harf
                            ex_letters.add(harf)
        
                else:
                    ex_letters.add(harf)
                    print(f"{can} kadar harf tahmin canınız kaldı") 
                    can -= 1
           
                    if can == 0 :
                        print("hakkınız bitti ")
                        break
                print("Kullanılan harfler")
                print(" ".join(ex_letters))
                print(" ".join(new_dizi))
                print("\n")

if can != 0: 
    print(f"bildiniz kelime = {kelime} ")



""" tahmin var- bu yapıldı
veri tabanından çekilecek kelimeler
yazdığın harfler silinsin
veri çek spor için 1 başka şey için 2 
 """
