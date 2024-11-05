# Input dari pengguna
ukuran = int(input("Masukkan ukuran sisi belah ketupat: "))
karakter = input("Masukkan karakter pilihan (misalnya X/O): ")

# Menghitung jumlah baris
total_baris = 2 * ukuran - 1

# Loop untuk setiap baris
for i in range(total_baris):
    # Menentukan jumlah spasi di awal baris
    if i < ukuran:
        spasi = ukuran - i- 1
    else:
        spasi = i- ukuran + 1

    # Mengecek spasi ketupat
    baris = ""
    for j in range(total_baris):
        if (j >= spasi and j < total_baris - spasi) and ((i + j) % 2 == 0): #dalam batas ketupat
            print(karakter, end="")
        else:
            print(" ", end="")
    print()