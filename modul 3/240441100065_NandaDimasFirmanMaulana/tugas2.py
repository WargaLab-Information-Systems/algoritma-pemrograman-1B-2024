#  2
angka = input("Masukan angka : ") 
angka_terbalik = ""
for i in range(len(angka) - 1, -1, -1):
    angka_terbalik += angka[i]
    print(i)