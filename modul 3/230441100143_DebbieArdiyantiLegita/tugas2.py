# Program untuk membalikkan urutan angka menggunakan perulangan

# Meminta pengguna memasukkan angka bulat
angka = int(input("Masukkan angka bulat: "))

# Inisialisasi variabel untuk menyimpan angka terbalik
angka_terbalik = 0

# Loop untuk membalikkan angka
while angka != 0:
    digit = angka % 10  # Mendapatkan digit terakhir
    angka_terbalik = angka_terbalik * 10 + digit  # Menambahkan digit ke angka terbalik
    angka = angka // 10  # Menghilangkan digit terakhir dari angka asli

# Menampilkan hasil angka yang sudah dibalikkan
print("Angka setelah dibalik: ", angka_terbalik)