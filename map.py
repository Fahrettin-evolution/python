sayilar=[1,3,5,7,9,10,19]

yeniliste=list(map(lambda x:x**2,sayilar))          #map(func,iterable) böyle olur burada iter=iterasyondur pythonda for döğüsü temeli
yeniliste1=[]                                                    #yani sayılar içinde gez demek
print(yeniliste)
filtre1=list(filter(lambda sayi:sayi<8,sayilar)) #bu işlemin aynısı map yaparsan filtre yerine sana ture false değerlerini döndürür
print(filtre1)                                   #burdaki bantık sayıyı çekmek
#for i in sayilar:        #birnevi for ün görevini yapıyor. 4 satırlık işlemi ikiye indiriyor
#    yeniliste1.append(i*i)
#print(yeniliste1)
from functools import reduce
sayilarinhepsininbiribiriilecarpimi=reduce(lambda x,y:x*y,sayilar)
print(sayilarinhepsininbiribiriilecarpimi)
#burada ilk önce 1 ve 3 alıyor x=1 y=3 bunları çarpıyor sonra x e atıyor
#sonra y 5 oluyor ve çarpıyor tekrardan x e atıyor bu sürec böyle devam ediyor.