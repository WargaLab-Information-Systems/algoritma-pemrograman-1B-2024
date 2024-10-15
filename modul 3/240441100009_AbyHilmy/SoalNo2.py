# Meminta pengguna memasukkan angka bulat
angka = input("Masukkan angka bulat: ")

# Membalikkan urutan angka
angka_balik = ""
for i in range(len(angka) - 1, -1, -1):
    angka_balik += angka[i]

# Menampilkan hasill
print(angka_balik)

