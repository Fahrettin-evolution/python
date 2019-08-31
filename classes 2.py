class person:
    def __init__(self,Firstname,Lastname,Age):
        self.FirstName=Firstname
        self.LastName=Lastname
        self.Age     =Age
x=int(input("Kaç kişi veri girmek istiyorsunuz="))
persons=[1,2,3,4,5,6,7,8,9,0]
for i in range(x):
    print(i)
    Name=input("Kullanıcı ismini giriniz")
    LastNAME=input("kullanıcı soyismi giriniz=")
    AGEe=int(input("kullanıcı yaşını giriniz="))
    persons[i]=person(Name,LastNAME,AGEe)
print(persons[0].FirstName)

class worker(person):
    def __init__(self,salary):
        self.salary=salary
class customer(person):
    def __init__(self,crediCardnumber):
        self.crediCardnumber=crediCardnumber
ahmet =worker()
ahmet.LastName #Ahmet yazdığımızda göreceksinki nokta yapın persommuda alcak

mehmet =customer()
mehmet.Age     #ayni işlem yukardaki gibi personda alacaksınız
