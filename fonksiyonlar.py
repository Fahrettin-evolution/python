#%%
def selamver(isim = "ziyaretçi",soyisim="arkadaş"):
    print("Merhaba " + isim + " "+ soyisim)
selamver()
selamver("fahrettin")
selamver("fahrettin","okur")
#%%
dikücgenalan = lambda a,b : a*b/2
print(dikücgenalan(3,2))
x=dikücgenalan = lambda a,b : a*b/2  # x atamada x artık fonksiyon oluyor fonk ataması yapabiliriz
print(x(5,10))
