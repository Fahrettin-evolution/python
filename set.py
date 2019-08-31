studentset ={"fahrettin","tugçe","ahmet"}      #en hızlı çaılışan bir yapıdır index olmadığı için bir sıralamk karışık gösteris verileri sana
#studentset = set("fahrettin","tuğçe","ahet")
print(studentset)

for student in studentset:
    print(student)

print("fahrettin" in studentset) #true ve false değeri döndürecek
print("Fahrettin" in studentset) #küçük ve büyük harf duyarlılığı var

if "fahrettin" in studentset:
    print("listede fahrettin ismi var")

studentset.add("kaan")  #listeye birşeyler ekleyebilirsin ama kaldırma işlemi yapamasın
print(studentset)

studentset.update(["mehmet","goksel","fevzi"])
print(studentset)

studentset.remove("mehmet")
print(len(studentset))

studentset.discard("mehmet")  #bu eğere mehemt var sa kaldır yoksa bana hata verme boş geç önemseme demek
print(len(studentset))

x=studentset.pop()    #kafasınsa göre bir veri siler
#studentset.clear()   #sadce setin içini temizler set durur
#del studentset       #burada set tamama ortadan kalkar
print(len(studentset))
print(x)
print(studentset)
print("\n\n\n\n")
      #set union  foksiyonu iki farklı seti birleştirir ve aynı olan iki elamanı tekrardan yazmaz
setA={1,2,3,4,5}
setB={4,5,6,7,8,9}
print(setA |  setB)
print(setA.union(setB))
print(setB.union(setA))

print(setA &  setB)         #bu olayda iki setin ortak olanı verir
print(setA.intersection(setB))
print(setB.intersection(setA))


print(setA -  setB)         #a fark b küme mantığı ikisnde  olmayanı alır
print(setA.difference(setB))
print(setB.difference(setA))


print(setA ^   setB)          #simtrik fark olarak geçiyor ortak olan çıkarıyor
print(setA.symmetric_difference(setB))
print(setB.symmetric_difference(setA))


print("\n\n\n\n\n")

my_sözlük = {
    "book":"kitap",
    "car":"araba"
}
sözlük =dict(kitap ="book",masa="table")
my_sözlük["book"]="kitap 1"
my_sözlük["pencil"]="kalem"
print(my_sözlük["book"])
print(my_sözlük)
del(my_sözlük["book"])
print(my_sözlük)


















