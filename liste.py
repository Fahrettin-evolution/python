my_students=["fahrettin","kaan","mehmet"]
print(my_students[0])
my_students.append("ahmet")
print(my_students[3])
my_students.remove("kaan")
print(my_students)
city = list(("adana","ankara"))
print(city)
print(city[0])
print(len(my_students))
#print(city.clear())       #bu listenin içini temizler.
my_students.append("ahmet")
my_students.append("ahmet")
print("benim öğrencilerimden ismi aynı olan sayısı =",my_students.count("ahmet"))
print("Ankaranın bulunduğu index="+str(city.index("ankara")))
print(my_students)
my_students.pop(1) #2 numaralı index i çıkarır
print(my_students)
my_students.insert(1,"veli")   #burada 1. indeksi çıkarmadı kaydırma işlemi yaptı.
print(my_students)
print(my_students.reverse())
print(my_students)
print("\n\n\n\n")


city2=city  #burada dizilerde listelerde aynı şeyi dünüyorsun ramdeki adresler eşit oldu her seferinde iksinede aynı adresten işlem yapacak
city.append("denizli")
print(city)
city2.append("izmir")
print(city2)

city3=city.copy()
city3.append("istanbul")
print(city3)                #burada iki farklı olay oldu
city.append("darende")
print(city)
print("\n\n\n\n\n")


my_students.reverse()
city.extend(my_students)
print(city)
city.sort()  #alfabetik sıraya göre dizer
print(city)