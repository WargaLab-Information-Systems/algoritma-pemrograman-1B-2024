# Meminta input ukuran (size)
size = int(input("Masukkan size: "))
# Menghitung nilai rumus sebagai setengah dari ukuran
rumus = int(size/2)

# Bagian Pertama: Cetak 3 garis vertikal bintang di tepi kanan
for x in range (1, rumus):
            # Cetak bintang di ujung kanan, dengan spasi sebelumnya
            print(" " * (size - 2) + "*")
            print(" " * (size - 2) + "*")
            print(" " * (size - 2) + "*")

print()
print()

# Bagian Kedua: Cetak kotak dengan bintang di tepi kiri dan kanan
for x in range (1, rumus):
            # Cetak bintang di tepi kiri dan kanan, dengan spasi di tengah
            print("*" + " " * (size - 2) + "*")
# Ulangi pola kotak
for y in range (1, rumus):
            print("*" + " " * (size - 2) + "*")
# Cetak garis penuh bintang di bagian bawah kotak
print("*" * size)
# Bagian akhir dari kotak, cetak 3 garis vertikal bintang di tepi kanan
print(" " * (size - 1) + "*")
print(" " * (size - 1) + "*")
print(" " * (size - 1) + "*")

print()
print()

# Bagian Ketiga: Pola horizontal dan garis kanan
# Cetak garis penuh bintang sebagai batas atas
print("*" * size)
# Cetak beberapa garis dengan bintang hanya di ujung kanan
for x in range(1, rumus):
            print(" " * (size - 1) + "*")
# Cetak lagi garis penuh bintang di tengah
print("*" * size)
# Cetak lagi beberapa garis dengan bintang di ujung kanan
for x in range(1, rumus):
            print(" " * (size - 1) + "*")
# Cetak garis penuh bintang sebagai batas bawah
print("*" * size)