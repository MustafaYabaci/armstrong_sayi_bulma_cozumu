sayi=int(input("lütfen bir sayı giriniz"))
toplam=0
basamak=str(sayi)
for i in basamak:
    rakam=int(i)**len(basamak)
    toplam+=rakam
if(sayi==toplam):
    print("sayı armstrong bir sayıdır")
else:
    print("sayı armstrong degıldır")