tupleliste =(2,3,4,"Adana",(5,7,6),[])
liste=[2,3,4,"Adana",[5,8,9],()]            #tuple de amaç tek seferde içlerine yazılarını yazrsın sonradan değiştiremesin.
print(type(tupleliste))
print(type(liste))
print(tupleliste)
print(liste)
print(len(tupleliste))
print(len(liste))
print("\n\n\n\n\n")
print(tupleliste[-2])
print(liste[-2])


print("\n\n\n\n\n")
print(tupleliste[1:2]) #gördüğünüz üzere virgül var
print(liste[1:2])
tupledeger =("fahrettin")
print(type(tupledeger))         #burada python bunu tuple olarak alğılamıyor onun için şu yapımalı
tupledeger1 =("fahrettin",)
print(type(tupledeger1))