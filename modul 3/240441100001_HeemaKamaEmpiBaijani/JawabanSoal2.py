#membalikkan angka
angka = int(input("masukkan angka bulat: "))
angkaInt= str(angka)
angka_balik = ""

while angkaInt:
    angka_balik += angkaInt[-1]
    angkaInt = angkaInt[:-1]
    
angka_balik = int(angka_balik)

print("membalikkan angka bulat:", angka_balik)