#class Matematik:
    #def toplam(self,say1,say2):
      #  print(self)
     #   return say1+say2
    #def cikarma(self,say1,say2):
    #    print(self)
   #     return say1-say2
    #def bolme(self,say1,say2):
    #    print(self)
    #    return say1/say2
   # def carpma(self,say1,say2):
  #      print(self)
 #       return say1*say2
#matematik=Matematik()   #bunu yaparsan artık bellkete matematik adında bir nese oluşuyor.
#print("toplamın soucu="+str(matematik.toplam(2,98)))
#self koymadan yaptığımızda matematik e karşılık gelen say1 oluyor bu yüzden self koydun print le gösterecem
#çalıştırdığımda görecemki self burada Matematik class adresinin temsil ediyor adresi temsil ediyor.
#print(matematik)

#ikisiarasındaki farklara bak yukardakine göre
class Matematik:
    def __init__(self,sayi1,sayi2):
        print("sistemi çalıştıdın ilk burası aktif")
        self.sayi1=sayi1                                         #self.sayi1=sayi1  self.sayi2=sayi2 genelde böyle yapılır
        self.sayi2=sayi2                                         #sen söyle yapabilrisin self.x=sayi1  self.y=sayi2
    def toplam(self):
     #   print(self)
        return self.sayi2+self.sayi1
    def cikarma(self):
     #   print(self)
        return self.sayi1-self.sayi2
    def bolme(self):
     #   print(self)
        return self.sayi1/self.sayi2
    def carpma(self):
     #   print(self)
        return self.sayi1*self.sayi2
x=int(input("Birinci sayiyi giriniz="))
y=int(input("ikinci sayiyi giriniz="))
matematik=Matematik(x,y) #bunun yapılması ilk olarak def __init__ içini çalıştırır parantezin içi boş olsada.
print("İki sayinin toplamı=" + str(matematik.toplam()))
print("İki sayinin farkı  =" + str(matematik.cikarma()))
print("İki sayinin bölümü =" + str(matematik.bolme()))
print("İki sayinin çarpımu=" + str(matematik.carpma()))