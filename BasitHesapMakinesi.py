def topla(sayi1,sayi2):
    return sayi1+sayi2
def cikar(sayi1,sayi2):
    return sayi1-sayi2
def carp(sayi1,sayi2):
    return sayi1*sayi2
def bolme(sayi1,sayi2):
    return sayi1/sayi2
Devam=True
while Devam:
    print("---------hannği işlemi yapacaksınız-------------")
    print("1.Toplama...")
    print("2.Çıkarma...")
    print("3.Çarpma....")
    print("4.Bölme.....")
    x=int(input("Yapacagınız işlemi seçiniz="))
    if x==1:
        sayi1=int(input("1.sayiyi girniz="))
        sayi2=int(input("2.sayiyi giriniz="))
        print("Toplamın sonucu="+str(topla(sayi1,sayi2)))
    elif x==2:
        sayi1 = int(input("1.sayiyi girniz="))
        sayi2 = int(input("2.sayiyi giriniz="))
        print("Çıkarmanın sonucu="+ str(cikar(sayi1,sayi2)))
    elif x==3:
        sayi1 = int(input("1.sayiyi girniz="))
        sayi2 = int(input("2.sayiyi giriniz="))
        print("Çarpmanın sonucu=" + str(carp(sayi1,sayi2)))
    else:
        sayi1 = int(input("1.sayiyi girniz="))
        sayi2 = int(input("2.sayiyi giriniz="))
        print("Bölmenin sonucu="+ str(bolme(sayi1,sayi2)))
    dev=input("Başka işlem yapmak istiyorsanız 1 e basınız=")
    if dev!= str(1):
        Devam=0
print("Sistemden çıktınız!!!")