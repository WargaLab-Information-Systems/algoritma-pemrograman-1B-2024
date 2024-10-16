#Meminta input dari pengguna
angka = input("masukkan angka bulat: ")

#Mengecek apakah angka negatif
if angka[0] == "-":
    #membalikkan angka tanpa tanda minus, lalu menambahkan tanda minus didepan
    angka_terbalik = "-"+ angka [:0:-1]
else:
    angka_terbalik = angka[::-1]

#Menampilkan hasilnya
print(f"angka setelah dibalik:", angka_terbalik)

