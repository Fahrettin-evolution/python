try:
 sayi=int(input("bir sayi giriniz:"))
 print(sayi)
except ValueError:
    print("hatalı bir değer girdiniz lütven tekrar giriniz!!!")
except ZeroDivisionError:
    print("Payda sıfır olamaz!!!")
except (ZeroDivisionError,EnvironmentError):
    print("Güzel hata oluşturdunuz")
except:
    print("Bir hata oluştu!!!")