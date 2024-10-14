# Meminta input dari pengguna
angka = input("Masukkan angka bulat: ")

# Membalik urutan angka menggunakan perulangan
if angka[0] == "-":
    angka_balik = "-"  # Menyimpan tanda minus di awal
    angka = angka[1:] # untuk menghilangkan tanda minus di awal
else:
        angka_balik = ""
for i in range(len(angka) - 1, -1, -1):
    angka_balik += angka[i]
# Menampilkan hasil
print("Angka setelah dibalik: ",angka_balik)