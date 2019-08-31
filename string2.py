text = "Merhaba Dünya"
print(text[:8])
len1=len(text)
print(text[len1-1])
print(text[-1]) #sondan başlayarak geri gider.
#Name= "Fahrettin"
#old = 21                              #len() fonksiyonu sadece sitringlerde kulanılır
#Name2 = "Ahmet"
#print(len(Name),"\n",len(Name2))

#print(text.upper())           #bu harfleri büyük yazmaya yarar
#print(text.lower())           #bu haflerin hepsisinin küçük yazmasınsa yarar


#text=text.replace("ü","u")     #text dosyasınını değiştirerek ü yerine u yapıyor
#print(text)
#print(text.replace("r","4"))



knowledge ="            fahrettin okur     dsfs fsdf   "
print(knowledge)
print(knowledge.strip())  #strip fonksiyonu baştaki ve sondaki boşlukları yok sayıyor
print(knowledge.split())   #böyle yaparsak boyluklara göre ayırır
knowledge="fahrettin okur1çok1444"
print(knowledge.split("1"))  #bir gördüğü yeri ayrım olarak kabul eder.
