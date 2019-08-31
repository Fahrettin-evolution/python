x=int(input("Bir sayi giriniz="))
y=int(input("İkinci sayiyi giriniz="))
z=int(input("Üçüncü sayiyi giriniz="))


if (x>=y) and (x>=z):
    büyüksayi=x
elif (y>=x) and (y>=z):
    büyüksayi=y
else:
    büyüksayi=z
print("En büyük sayi:",büyüksayi)