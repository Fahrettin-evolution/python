import sys #bu sistemdeki hatanın ne olduğunu veriri

data=[7,"araba",23,"7",0]

for x in data:
    try:
        print("sayi  :" + str(x))
        sonuc = 1/int(x)
        print("sonuç  :" + str(sonuc))
    except ValueError:
        print(str(x) + " Bu bir sayı değil")
    except ZeroDivisionError:
        print(str(x) + " İçin sıfıra bölme hatası")
    except:
         print(str(x) + " Hesaplanamadı")             #yukardaki ilk iki kısmı yorum satırı yaparsanız hatayı tek tek söyler.
         print("Sistem diyor ki :" + str(sys.exc_info()[0]))
    finally: #bu her koşulda çalışır yani hata alsın almasın
        print("\n\n\nİşlemler bitti")

#try except  önemi mesela bir dosya açtınız hata aldı eğer alırsa dosya açık kalmasın diye finally kullanırsın dosya kapanır.
#ayrıyeten gördünüz gibi başta hata almasına karşın sistem durmadı çalışmaya devam etti bunun için kullanılır.