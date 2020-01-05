print("1. .isalnum boşluk varsa False yazar")
isim = "M234a"
print(isim.isalnum())#isalnum=boşluk varsa False yoksa True
isim = "M3a l22"
print(isim.isalnum())

print("2. .isalpha= sadece sayı varsa true")
isim= "isalpha"
print(isim.isalpha())

print("3. .upper=farleri büyütür")
isim="abc"
print(isim.upper())

print("4. .startswith()= eğer baş harfi a ise True")
isim="aismail61"
print(isim.startswith("a"))
print("5. .endswith()= eğer son harfi a ise True")
isim="ismail61a"
print(isim.endswith("a"))

print("6. .islower= eğer büyük harf içeriyorsa False")
isim="ismail61"
print(isim.islower())

print("7. .isupper= eğer hepsi büyükse True")
isim="İSMAİL61"
print(isim.isupper())

print("8. .upper= yazıları büyük harfe dönüştürür")
isim="ismail61"
print(isim.upper())

print("9. .replace= a yerine virgülden sonra yazılanlar yazılır")
isim="ismaila"
print(isim.replace("a","61"))
