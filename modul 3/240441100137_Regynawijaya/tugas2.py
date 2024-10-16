angka = int(input("masukkan bilangan bulat:"))

strangka = str(angka)

strbalik = ""

for i in range(len(strangka)-1,-1,-1):
    strbalik+=strangka[i]
    
print(strbalik)