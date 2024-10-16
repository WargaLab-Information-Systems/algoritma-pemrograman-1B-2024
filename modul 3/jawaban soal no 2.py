angka = input("Masukan angka bulat:")
angkabalik= ""
for i in range(len(angka)-1,-1,-1):
    angkabalik +=angka[ i ]
    print("Angka setelah dibalik:",angkabalik)