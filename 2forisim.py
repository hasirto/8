isim=input("isminiz: ")
if isim =="  ":
    print("2 boşluk girdiniz")

for i in range(len(isim)):
    print("isminizin {}.ci harfi {}'dir.".format(i+1,isim[i]))